import os
from rembg import remove
from PIL import Image
import io

def remove_bg_to_white(input_folder, output_folder):
    # Make sure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            with open(input_path, "rb") as inp_file:
                input_data = inp_file.read()

            # Remove background
            result = remove(input_data)
            result_img = Image.open(io.BytesIO(result)).convert("RGBA")

            # Create white background
            white_bg = Image.new("RGBA", result_img.size, (255, 255, 255, 255))
            final_img = Image.alpha_composite(white_bg, result_img)

            # Save as RGB (no transparency)
            final_img = final_img.convert("RGB")
            final_img.save(output_path)

            print(f"Processed: {filename} → {output_path}")

# Example usage
input_folder = "input_images"
output_folder = "output_images"
remove_bg_to_white(input_folder, output_folder)
