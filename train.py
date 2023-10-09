import keras
from keras import backend as K
from keras.preprocessing.image import ImageDataGenerator#
import keras.applications
from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import Adam



train_dir = 'train_labeled'
test_dir = 'test_labeled'
valid_dir = 'valid_labeled'

train_batches = ImageDataGenerator().flow_from_directory(train_dir, target_size = (224,224),
                                                         classes=["Bouteille","Plastique","goblet plastique","goblet en papier","metal","carton","vide"],batch_size=32)
test_batches = ImageDataGenerator().flow_from_directory(test_dir, target_size = (224,224),
                                                         classes=["Bouteille","Plastique","goblet plastique","goblet en papier","metal","carton","vide"],batch_size=10)
valid_batches = ImageDataGenerator().flow_from_directory(valid_dir, target_size = (224,224),
                                                         classes=["Bouteille","Plastique","goblet plastique","goblet en papier","metal","carton","vide"],batch_size=7)

vgg16_model = keras.applications.vgg16.VGG16()
model = Sequential()
for layer in vgg16_model.layers:
    model.add(layer)

model.layers.pop()

for i in range(len(model.layers)-3):
    model.layers[i].trainable = False

model.add(Dense(7,  activation = 'softmax'))

model.compile(Adam(lr=.001), loss = 'categorical_crossentropy',metrics=['accuracy'])



model.fit(train_batches, steps_per_epoch=100,
                    validation_data=valid_batches, validation_steps=10, epochs=8,
                    verbose =2)



model.save("model8")
