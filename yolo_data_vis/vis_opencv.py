"""
Usage:
  yolo_data_vis DIR_IMAGES DIR_LABELS
"""
from docopt import docopt
import cv2
from .utils import get_images_labels, draw_bounding_boxes
import os 

# Function to display images and navigate using arrow keys
def visualize_images(dir_images, dir_labels):
    image_files = get_images_labels(dir_images, dir_labels)
    current_index = 0

    while True:
        image_path, label_path = image_files[current_index]
        image = draw_bounding_boxes(image_path, label_path)

        if image is not None:
            cv2.imshow('Image Viewer', image)
            key = cv2.waitKeyEx(0)
            # Handle keyboard inputs
            if key == ord('q'):
                break  # Quit the viewer
            elif key == 65361:  # Left arrow key
                current_index = (current_index - 1) % len(image_files)  # Previous image
            elif key == 65363:  # Right arrow key
                current_index = (current_index + 1) % len(image_files)  # Next image

        else:
            print(f"Error loading image: {image_path}")

    cv2.destroyAllWindows()


def main():
    arguments = docopt(__doc__)
    dir_images = arguments['DIR_IMAGES']
    dir_labels = arguments['DIR_LABELS']
    visualize_images(dir_images, dir_labels)
    

if __name__ == '__main__':
    main()
    
