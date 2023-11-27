from PIL import Image
from pillow_heif import register_heif_opener
import os

register_heif_opener()

old_directory='C:/Users/Liqaa Arttouch/Desktop/hali/'
new_directory='C:/Users/Liqaa Arttouch/Desktop/hali_1/'

for filename in os.listdir(old_directory):
    file_extantion = '.heic'
    if filename.lower().endswith(file_extantion):
        image = Image.open(os.path.join(old_directory, filename))

        if not os.path.exists(new_directory):
            os.makedirs(new_directory)

        image_path = new_directory+filename.lower().removesuffix(file_extantion)+'.png'
        print(image_path)
        image.save(image_path)
