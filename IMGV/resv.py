from PIL import Image
import os

# Input and output folders
input_folder = "./input"
output_folder = "./output"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Desired size for VITON-HD
target_size = (768, 1024)  # (width, height)

# Process all images in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
        input_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + ".jpg"
        output_path = os.path.join(output_folder, output_filename)

        # Open and resize image
        with Image.open(input_path) as img:
            resized_img = img.resize(target_size, Image.Resampling.LANCZOS)

            # Convert to RGB to avoid errors when saving as JPG
            if resized_img.mode != "RGB":
                resized_img = resized_img.convert("RGB")

            # Save as .jpg
            resized_img.save(output_path, "JPEG", quality=95)

        print(f"✅ Processed: {filename} → {output_filename}")

print("\n🎉 All images resized to 768×1024 and saved as JPGs in the output folder.")
