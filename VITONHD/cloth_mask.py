import os
import cv2
import numpy as np
from rembg import remove

# Input folder (cloth images)
input_folder = "datasets/raw/"
# Output folder (binary masks)
output_folder = "datasets/test/cloth-mask/"

os.makedirs(output_folder, exist_ok=True)

# Supported image formats
valid_exts = [".jpg", ".jpeg", ".png"]

for filename in os.listdir(input_folder):
    if any(filename.lower().endswith(ext) for ext in valid_exts):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")

        # Run rembg
        with open(input_path, "rb") as inp:
            result = remove(inp.read())

        # Convert result to numpy image
        nparr = np.frombuffer(result, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

        # Extract alpha channel
        alpha = image[:, :, 3]

        # Convert to pure black & white mask
        _, binary_mask = cv2.threshold(alpha, 127, 255, cv2.THRESH_BINARY)

        # Save mask
        cv2.imwrite(output_path, binary_mask)
        print(f"✅ Saved mask: {output_path}")

print("🎉 All cloth masks generated!")
