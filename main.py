# =============================================================================
# Bulk Image Converter
# =============================================================================

# This application aims to do the following things:
# - Detect "blue" parts in the image
# - Change blue parts to black
# - Generate a new image with the changes

# Libraries
import cv2
import numpy as np
import os
from loguru import logger
from glob import glob

# Directories
input_dir = "input_folder"  
output_dir = "output_folder"
os.makedirs(output_dir, exist_ok=True)

# Interation through all folders
for image_path in glob(f"{input_dir}/*.jpg"):
    image = cv2.imread(image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 
    
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])
    
    # Mask creation
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Replacment
    image[mask > 0] = [0, 0, 0]
    
    # Output
    output_path = os.path.join(output_dir, os.path.basename(image_path))

    if cv2.imwrite(output_path, image) == True:
        logger.success(f"Image successfully saved to {output_path}")

    else:
        logger.error(f"An error occurred while saving the image to {output_path}")

logger.success(f"Processed images saved to {output_dir}")