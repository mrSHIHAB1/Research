from PIL import Image
import os

def resize_images(input_folder, output_folder, target_size=(256, 256)):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                with Image.open(input_path) as img:
                    img = img.convert("RGB")  
                    resized_img = img.resize(target_size)
                    resized_img.save(output_path)
                    print(f"Resized: {filename}")
            except Exception as e:
                print(f"Error resizing {filename}: {e}")

 
input_dir = r"C:\path\to\your\original_images"
output_dir = r"C:\path\to\your\resized_images"
resize_images(input_dir, output_dir, target_size=(256, 256))
