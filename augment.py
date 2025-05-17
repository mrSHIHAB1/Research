import os
import cv2
import albumentations as A

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

transform = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.3),
    A.Rotate(limit=20, p=0.5),
    A.GaussianBlur(blur_limit=3, p=0.3)
])

def augment_folder(input_dir, output_dir):
    ensure_dir(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".jpg"):
            input_path = os.path.join(input_dir, filename)
            image = cv2.imread(input_path)

            if image is None:
                print(f"Could not read image: {filename}")
                continue

            cv2.imwrite(os.path.join(output_dir, filename), image)

            augmented = transform(image=image)['image']
            name, ext = os.path.splitext(filename)
            aug_filename = f"{name}_aug{ext}"
            aug_path = os.path.join(output_dir, aug_filename)

            cv2.imwrite(aug_path, augmented)
            print(f"Augmented: {aug_filename}")

# Set your folder paths
input_dir = "D:/old/Corn leaf/Corn leaf/Healthy"
output_dir = "D:/old/Corn leaf/Corn leaf/Healthy_augmented"

augment_folder(input_dir, output_dir)
