import os

def convert_JPG_to_jpg(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".JPG"):
            old_path = os.path.join(folder_path, filename)
            new_filename = filename[:-4] + ".jpg"
            new_path = os.path.join(folder_path, new_filename)
            
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")

folder = r"C:\Users\vecis\OneDrive\Desktop\corn\CORNDATA_M\Northern Leaf Blight"
convert_JPG_to_jpg(folder)
