from PIL import Image
import os

# Input and output folders
input_folder = "./inputg"
output_folder = "./outputg"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Desired size for VITON-HD
target_size = (620, 420)  # (width, height)

# Process all images in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.jpg")

        # Open image
        img = Image.open(input_path)

        # Resize using NEAREST (to preserve label map integrity)
        resized = img.resize(target_size, Image.NEAREST)

        # Save resized image
        resized.save(output_path)
        print(f"✅ Saved resized parsing map: {output_path}")
