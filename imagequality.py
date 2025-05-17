import os
from PIL import Image

def reduce_image_quality_batch(input_folder, output_folder, quality=50):
    """
    Reduces the quality of all JPEG images in a folder and saves them in the output folder.
    
    Parameters:
        input_folder (str): Path to the folder with original images.
        output_folder (str): Path where reduced quality images will be saved.
        quality (int): Quality of the saved image (1–95). Lower means more compression.
    """
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                with Image.open(input_path) as img:
                    # Convert PNG to JPEG if needed
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")

                    # Save with reduced quality
                    img.save(output_path, quality=quality, optimize=True)
                    print(f"Saved: {output_path}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

# Example usage
input_folder = "D:/old/Corn leaf/Corn leaf/Healthy_augmented"
output_folder = "D:/old/Corn leaf/Corn leaf/rha"
reduce_image_quality_batch(input_folder, output_folder, quality=50)
