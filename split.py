import os
import shutil

source_path = '/home/hyr/Desktop/Cat-Recognition/photos/input_data'
mati_destination = '/home/hyr/Desktop/human/mati'
rys_destination = '/home/hyr/Desktop/human/rys'

i = 0

files = os.listdir(source_path)

for file in files:
    print(file)
    #if os.path.splitext(file)[2] == '.jpg':
    if file.startswith('cat'):
        if i < 400:
            shutil.move(os.path.join(source_path, file), mati_destination)
        elif i >= 400:
            shutil.move(os.path.join(source_path, file), rys_destination)
        i += 1
    if i == 800:
        break