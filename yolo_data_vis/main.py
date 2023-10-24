"""
Usage:
  yolo_data_vis DIR_IMAGES DIR_LABELS
"""
from docopt import docopt
import cv2
import os
from glob import glob 


# Function to get a list of image files in a directory
def get_images_labels(dir_images, dir_labels):
    image_files = glob(os.path.join(dir_images, '*jpg'))
    label_files = glob(os.path.join(dir_labels, '*txt'))

    image_files = sorted(image_files, key= lambda x: os.path.basename(x))
    label_files = sorted(label_files, key= lambda x: os.path.basename(x))
    return list(zip(image_files, label_files))


def draw_bounding_boxes(image_path, label_path):
    image = cv2.imread(image_path)
    image_height, image_width, _ = image.shape
    with open(label_path, 'r') as file:
        for line in file:
            class_id, x, y, width, height = map(float, line.strip().split())
            x, y, width, height = int(x * image_width), int(y * image_height), int(width * image_width), int(height * image_height)
            
            # Draw the bounding box
            color = (0, 255, 0)  # BGR color format (green)
            thickness = 2
            cv2.rectangle(image, (x - width // 2, y - height // 2), (x + width // 2, y + height // 2), color, thickness)
            label = str(class_id) #labels[int(class_id)]
            cv2.putText(image, label, (x - width // 2, y - height // 2 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness)

    return image



# Function to display images and navigate using arrow keys
def visualize_images(dir_images, dir_labels):
    image_files = get_images_labels(dir_images, dir_labels)
    current_index = 0

    while True:
        image_path, label_path = image_files[current_index]
        print(os.path.basename(image_path))
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
    
