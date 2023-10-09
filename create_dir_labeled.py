import os
import shutil



images_path = 'CYTECH_USER/CYTECH_DATA/valid/images'
labels_path = 'CYTECH_USER/CYTECH_DATA/valid/labels'

images = os.listdir(images_path)

os.makedirs('./valid_labeled')

names = ['Bouteille',"Plastique","goblet plastique","goblet en papier","metal","carton","vide"]

for name in names:
    os.makedirs('./valid_labeled/'+ name)


for image in images:
    f = open(labels_path+'/'+image.replace('.jpg', '.txt'))
    data = f.read()
    lenght = len(data)
    if lenght > 0:
        place = int(data[0])
    else:
        place = 6
    shutil.move(images_path+'/'+image, './valid_labeled/' + names[place])
    f.close()



