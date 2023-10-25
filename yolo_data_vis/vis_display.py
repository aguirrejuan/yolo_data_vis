"""
Usage:
  yolo_data_vis_jupyter DIR_IMAGES DIR_LABELS
"""
from docopt import docopt
import os
import ipywidgets as widgets
from IPython.display import display, Image, clear_output
from .utils import get_images_labels, draw_bounding_boxes

def display_images(dir_images, dir_labels):

    image_files = get_images_labels(dir_images, dir_labels)
    
    # Initialize the index for the current image
    current_image_index = 0

    # Create a function to display the current image
    def display_image(image_index):
        image_path, label_path = image_files[current_image_index]
        image = draw_bounding_boxes(image_path, label_path)
        return Image(data=image, width=400, height=400)

    # Create buttons for navigating through images
    prev_button = widgets.Button(description="Previous")
    next_button = widgets.Button(description="Next")

    # Create an output widget for displaying the image
    image_output = widgets.Output()

    # Create a function to handle button clicks
    def on_prev_button_click(b):
        nonlocal current_image_index
        current_image_index = (current_image_index - 1) % len(image_files)
        with image_output:
            clear_output(wait=True)
            display(display_image(current_image_index))

    def on_next_button_click(b):
        nonlocal current_image_index
        current_image_index = (current_image_index + 1) % len(image_files)
        with image_output:
            clear_output(wait=True)
            display(display_image(current_image_index))

    # Bind the button click functions to the buttons
    prev_button.on_click(on_prev_button_click)
    next_button.on_click(on_next_button_click)

    # Display the initial image
    with image_output:
        display(display_image(current_image_index))

    # Create a layout for the buttons
    buttons_layout = widgets.HBox([prev_button, next_button])

    # Display the buttons and the image output
    display(buttons_layout)
    display(image_output)



def main():
    arguments = docopt(__doc__)
    dir_images = arguments['DIR_IMAGES']
    dir_labels = arguments['DIR_LABELS']
    display_images(dir_images, dir_labels)
    
if __name__ == '__main__':
    main()
    