
import cv2
from glob import glob 
import os 

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

    image_name = os.path.basename(image_path).split('.')[0]
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

    
    cv2.putText(image, image_name, (0, 15),
                         cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                         (255, 0, 0),
                         thickness)
    return image
