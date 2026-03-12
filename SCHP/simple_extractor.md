
#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@Author  :   Peike Li (modified by assistant)
@Contact :   peike.li@yahoo.com
@File    :   simple_extractor.py
@Time    :   8/30/19 8:59 PM
@Desc    :   Simple Extractor with fixed color palettes for LIP/ATR
@License :   This source code is licensed under the license found in the
             LICENSE file in the root directory of this source tree.
"""

import os
import torch
import argparse
import numpy as np
from PIL import Image
from tqdm import tqdm

from torch.utils.data import DataLoader
import torchvision.transforms as transforms

import networks
from utils.transforms import transform_logits
from datasets.simple_extractor_dataset import SimpleFolderDataset

dataset_settings = {
    'lip': {
        'input_size': [473, 473],
        'num_classes': 20,
        'label': ['Background', 'Hat', 'Hair', 'Glove', 'Sunglasses', 'Upper-clothes', 'Dress', 'Coat',
                  'Socks', 'Pants', 'Jumpsuits', 'Scarf', 'Skirt', 'Face', 'Left-arm', 'Right-arm',
                  'Left-leg', 'Right-leg', 'Left-shoe', 'Right-shoe']
    },
    'atr': {
        'input_size': [512, 512],
        'num_classes': 18,
        'label': ['Background', 'Hat', 'Hair', 'Sunglasses', 'Upper-clothes', 'Skirt', 'Pants', 'Dress', 'Belt',
                  'Left-shoe', 'Right-shoe', 'Face', 'Left-leg', 'Right-leg', 'Left-arm', 'Right-arm', 'Bag', 'Scarf']
    },
    'pascal': {
        'input_size': [512, 512],
        'num_classes': 7,
        'label': ['Background', 'Head', 'Torso', 'Upper Arms', 'Lower Arms', 'Upper Legs', 'Lower Legs'],
    }
}


def get_arguments():
    """Parse all the arguments provided from the CLI."""
    parser = argparse.ArgumentParser(description="Self Correction for Human Parsing")

    parser.add_argument("--dataset", type=str, default='lip', choices=['lip', 'atr', 'pascal'])
    parser.add_argument("--model-restore", type=str, default='', help="restore pretrained model parameters.")
    parser.add_argument("--gpu", type=str, default='0', help="choose gpu device.")
    parser.add_argument("--input-dir", type=str, default='', help="path of input image folder.")
    parser.add_argument("--output-dir", type=str, default='', help="path of output image folder.")
    parser.add_argument("--logits", action='store_true', default=False, help="whether to save the logits.")

    return parser.parse_args()


def get_palette(dataset):
    """Return fixed color palette depending on dataset."""

    if dataset == 'lip':  # 20 classes
        return [
            0, 0, 0,        # Background
            128, 0, 0,      # Hat
            255, 0, 0,      # Hair
            0, 85, 0,       # Glove
            170, 0, 51,     # Sunglasses
            255, 85, 0,     # Upper-clothes
            0, 0, 85,       # Dress
            0, 119, 221,    # Coat
            85, 85, 0,      # Socks
            0, 85, 85,      # Pants
            85, 51, 0,      # Jumpsuits
            52, 86, 128,    # Scarf
            0, 128, 0,      # Skirt
            0, 0, 255,      # Face
            51, 170, 221,   # Left-arm
            0, 255, 255,    # Right-arm
            85, 51, 85,     # Left-leg
            255, 255, 0,    # Right-leg
            153, 51, 0,     # Left-shoe
            204, 255, 51    # Right-shoe
        ]

    elif dataset == 'atr':  # 18 classes
        return [
            0, 0, 0,        # Background
            128, 0, 0,      # Hat
            255, 0, 0,      # Hair
            0, 85, 0,       # Sunglasses
            170, 0, 51,     # Upper-clothes
            255, 85, 0,     # Skirt
            0, 0, 85,       # Pants
            0, 119, 221,    # Dress
            85, 85, 0,      # Belt
            0, 85, 85,      # Left-shoe
            85, 51, 0,      # Right-shoe
            52, 86, 128,    # Face
            0, 128, 0,      # Left-leg
            0, 0, 255,      # Right-leg
            51, 170, 221,   # Left-arm
            0, 255, 255,    # Right-arm
            85, 51, 85,     # Bag
            255, 255, 0     # Scarf
        ]

    elif dataset == 'pascal':  # generic VOC style palette
        n = dataset_settings['pascal']['num_classes']
        palette = [0] * (n * 3)
        for j in range(0, n):
            lab = j
            i = 0
            while lab:
                palette[j * 3 + 0] |= (((lab >> 0) & 1) << (7 - i))
                palette[j * 3 + 1] |= (((lab >> 1) & 1) << (7 - i))
                palette[j * 3 + 2] |= (((lab >> 2) & 1) << (7 - i))
                i += 1
                lab >>= 3
        return palette

    else:
        raise ValueError(f"Unsupported dataset: {dataset}")


def main():
    args = get_arguments()

    gpus = [int(i) for i in args.gpu.split(',')]
    assert len(gpus) == 1
    if not args.gpu == 'None':
        os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu

    num_classes = dataset_settings[args.dataset]['num_classes']
    input_size = dataset_settings[args.dataset]['input_size']
    label = dataset_settings[args.dataset]['label']
    print("Evaluating total class number {} with {}".format(num_classes, label))

    model = networks.init_model('resnet101', num_classes=num_classes, pretrained=None)

    state_dict = torch.load(args.model_restore)['state_dict']
    from collections import OrderedDict
    new_state_dict = OrderedDict()
    for k, v in state_dict.items():
        name = k[7:]  # remove `module.`
        new_state_dict[name] = v
    model.load_state_dict(new_state_dict)
    model.cuda()
    model.eval()

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.406, 0.456, 0.485], std=[0.225, 0.224, 0.229])
    ])
    dataset = SimpleFolderDataset(root=args.input_dir, input_size=input_size, transform=transform)
    dataloader = DataLoader(dataset)

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    palette = get_palette(args.dataset)

    with torch.no_grad():
        for idx, batch in enumerate(tqdm(dataloader)):
            image, meta = batch
            img_name = meta['name'][0]
            c = meta['center'].numpy()[0]
            s = meta['scale'].numpy()[0]
            w = meta['width'].numpy()[0]
            h = meta['height'].numpy()[0]

            output = model(image.cuda())
            upsample = torch.nn.Upsample(size=input_size, mode='bilinear', align_corners=True)
            upsample_output = upsample(output[0][-1][0].unsqueeze(0))
            upsample_output = upsample_output.squeeze()
            upsample_output = upsample_output.permute(1, 2, 0)  # CHW -> HWC

            logits_result = transform_logits(upsample_output.data.cpu().numpy(), c, s, w, h, input_size=input_size)
            parsing_result = np.argmax(logits_result, axis=2)
            parsing_result_path = os.path.join(args.output_dir, img_name[:-4] + '.png')
            output_img = Image.fromarray(np.asarray(parsing_result, dtype=np.uint8))
            output_img.putpalette(palette)
            output_img.save(parsing_result_path)

            if args.logits:
                logits_result_path = os.path.join(args.output_dir, img_name[:-4] + '.npy')
                np.save(logits_result_path, logits_result)

    return


if __name__ == '__main__':
    main()


