

import numpy as np
from PIL import Image

# 1️⃣ Load the mask in grayscale mode
mask_path = "person.png"  # update to your real path
mask = Image.open(mask_path).convert("L")
mask = np.array(mask)

print("Before:", np.unique(mask))

# 2️⃣ Replace invalid label IDs
mask[mask == 179] = 178   # replaces all pixels labeled 179 with 178

# Optional: clamp all IDs above 178 just in case
mask = np.minimum(mask, 178)

print("After:", np.unique(mask))

# 3️⃣ Save back to file
Image.fromarray(mask.astype(np.uint8)).save("person_gray_fixed.png")
print("✅ Saved as person_gray_fixed.png")


