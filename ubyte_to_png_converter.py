import os
import struct
import numpy as np
from PIL import Image

# Function to load MNIST data from .ubyte files
def load_mnist_images(filename):
    with open(filename, 'rb') as f:
        # Read the header information
        magic, num, rows, cols = struct.unpack(">IIII", f.read(16))
        # Read the image data
        images = np.fromfile(f, dtype=np.uint8).reshape(num, rows, cols)
        return images

# Path to your MNIST .ubyte file
images_path = 'D:/Downloads/archive (2)/t10k-images.idx3-ubyte'  # Update with your path
output_folder = 'D:/Downloads/archive (2)/images'           # Folder to save images

# Load images
images = load_mnist_images(images_path)

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Save each image as a PNG file
for i, img in enumerate(images):
    im = Image.fromarray(img)
    im.save(os.path.join(output_folder, f'mnist_{i}.png'))

    if i % 1000 == 0:  # Print progress every 1000 images
        print(f'Saved {i} images')

print(f"All images saved in '{output_folder}'")