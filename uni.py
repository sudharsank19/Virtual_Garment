

import numpy as np
from PIL import Image

mask = Image.open("person.png").convert("L")  # grayscale → IDs 0–19
mask = np.array(mask)

print("Unique IDs in mask:", np.unique(mask))

