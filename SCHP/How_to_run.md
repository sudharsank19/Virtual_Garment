

REM === Run extractor ===

python simple_extractor.py --dataset lip --model-restore checkpoints/exp-schp-201908261155-lip.pth --input-dir ./samples/person/ --output-dir ./results/parse/


python simple_extractor.py --dataset atr --model-restore checkpoints/exp-schp-201908301523-atr.pth --input-dir ./samples/person/ --output-dir ./results/parse/


