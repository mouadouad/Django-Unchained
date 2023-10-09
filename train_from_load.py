import keras
from keras import backend as K
from keras.preprocessing.image import ImageDataGenerator#
import keras.applications
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense, Flatten
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy



train_dir = 'train_labeled'
test_dir = 'test_labeled'
valid_dir = 'valid_labeled'

train_batches = ImageDataGenerator().flow_from_directory(train_dir, target_size = (224,224),
                                                         classes=["Bouteille","Plastique","goblet plastique","goblet en papier","metal","carton","vide"],batch_size=32)
test_batches = ImageDataGenerator().flow_from_directory(test_dir, target_size = (224,224),
                                                         classes=["Bouteille","Plastique","goblet plastique","goblet en papier","metal","carton","vide"],batch_size=10)
valid_batches = ImageDataGenerator().flow_from_directory(valid_dir, target_size = (224,224),
                                                         classes=["Bouteille","Plastique","goblet plastique","goblet en papier","metal","carton","vide"],batch_size=7)


model = keras.models.load_model('model3')

model.compile(Adam(lr=.0001), loss = 'categorical_crossentropy',metrics=['accuracy'])



model.fit(train_batches, steps_per_epoch=100,
                    validation_data=valid_batches, validation_steps=10, epochs=10,
                    verbose =2)



model.save("model9")
