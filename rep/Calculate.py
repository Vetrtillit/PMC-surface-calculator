import cv2
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog, Tk
import os
# Constant section
fractions = 12 # number of sectors
inner_radius = 40  # Inner circle radious
outer_radius = 535  # Outer radius radius. 
# Last two are needed to exclude technical information placed in the corners of the image from being calculcated as 

# Creating mask to differentiate both workspace circle from technical info and sectors of this circle from each other
def slice_mask(image, center, inner_radius, outer_radius, start_angle, end_angle):
    h, w = image.shape[:2]
    mask = np.zeros((h, w), dtype=np.uint8)

    # Defining start and end points for corresponding angles
    start_point = (int(center[0] + outer_radius * np.cos(np.radians(start_angle))),
                   int(center[1] + outer_radius * np.sin(np.radians(start_angle))))
    end_point = (int(center[0] + outer_radius * np.cos(np.radians(end_angle))),
                 int(center[1] + outer_radius * np.sin(np.radians(end_angle))))

    # Creating borderlines between sectors
    cv2.line(mask, center, start_point, 255, 1)
    cv2.line(mask, center, end_point, 255, 1)

    # Creating arcs of inner and outer radius
    cv2.ellipse(mask, center, (outer_radius, outer_radius), 0, start_angle, end_angle, 255, -1)
    cv2.ellipse(mask, center, (inner_radius, inner_radius), 0, start_angle, end_angle, 0, -1)
    return mask

# Making GUI asking for image directory
root = tk.Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()
root.destroy()


# Making GUI asking for background image
def choose_background():
    def set_north():
        global background_path
        background_path = 'without_pmc.png'
        selection_window.destroy()

    def set_south():
        global background_path
        background_path = 'without_pmc_south.png'
        selection_window.destroy()

    selection_window = tk.Tk()
    selection_window.title("Select a background image")

    label = tk.Label(selection_window, text="Select a background image: ")
    label.pack(pady=10)

    button_north = tk.Button(selection_window, text="North", command=set_north)
    button_north.pack(side="left", padx=20, pady=20)

    button_south = tk.Button(selection_window, text="South", command=set_south)
    button_south.pack(side="right", padx=20, pady=20)

    selection_window.mainloop()


# Launch the selection function (defined above)
choose_background()

# Reading the background image in grayscale
background = cv2.imread(background_path, cv2.IMREAD_GRAYSCALE)
# The constant of conversion between pixels of the image and square kilometers, it is given within the dataset with the images
PIXEL_TO_KM2 = 7.5

# Surface area calculating function
def calculate_sector_areas(image, background):
    # Background substraction
    foreground = cv2.absdiff(image, background)
    # Setting a threshold to exclude dim pixels (most of them are a part of the background that wasn't substracted)
    _, thresh = cv2.threshold(foreground, 20, 255, cv2.THRESH_BINARY)
    # Definition of the center and radius
    center = (int(image.shape[0] / 2), int(image.shape[1] / 2))
    radius = min(center)
    # Calculating 
    sector_areas = np.zeros(12)
    for i in range(12):
        start_angle = 90 - (i + 1) * 30
        end_angle = 90 - (i) * 30 

        # Combining earlier definitions for convenience
        sector_mask = slice_mask(image, center, inner_radius, outer_radius, start_angle, end_angle)

        # Applying mask and counting non-masked pixels in the sector
        sector_pixels = np.sum(cv2.bitwise_and(thresh, thresh, mask=sector_mask) > 0)

        # Converting counted pixels to square kilometers
        sector_area = sector_pixels * PIXEL_TO_KM2
        sector_areas[i] = sector_area    # Giving numbers to sectors

    return sector_areas


# Creating DataFrame to print results
results_df = pd.DataFrame(columns=[f'Sector {i+1}' for i in range(fractions)])

# Reading files and sorting them
image_filenames = [filename for filename in os.listdir(folder_selected) if filename.endswith(".png")]
image_filenames.sort()  # Сортировка имен файлов, если требуется

for index, filename in enumerate(image_filenames, start=1):
    filepath = os.path.join(folder_selected, filename)
    image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    sector_areas = calculate_sector_areas(image, background)

    # Adding calculation results for each image and its sectors
    results_df.loc[f'№ {index}'] = sector_areas

# Creating Excel sheet with these results
excel_path = os.path.join(folder_selected, 'surface_area.xlsx')
results_df.to_excel(excel_path, index_label='№')

# DEBUG
print(f'Results saved to {excel_path}')
