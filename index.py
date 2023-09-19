import os
from PIL import Image

# Define the folder containing PNG files and the output GIF file name
png_folder = 'PNGs'
output_gif_filename = 'output.gif'

# List all PNG files in the specified folder
png_files = [f for f in os.listdir(png_folder) if f.endswith('.png')]

if not png_files:
    print(f"No PNG files found in '{png_folder}'")
else:
    # Sort the PNG files to ensure the frames are in the desired order
    png_files.sort()

    # Create a list to store image frames
    frames = []

    for png_file in png_files:
        # Open and append each PNG file to the frames list
        image = Image.open(os.path.join(png_folder, png_file))
        frames.append(image)

    # Save the frames as a GIF file
    frames[0].save(
        output_gif_filename,
        save_all=True,
        append_images=frames[1:],
        duration=1000,  # Set the duration between frames in milliseconds
        loop=0,  # Loop indefinitely
    )

    print(f"GIF file '{output_gif_filename}' created with {len(frames)} frames.")
