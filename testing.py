from keras.preprocessing.image import ImageDataGenerator#
from tensorflow import keras
import numpy as np


test_dir = 'test_labeled'

test_batches = ImageDataGenerator().flow_from_directory(test_dir, target_size = (224,224),
                                                         classes=["Bouteille","Plastique","goblet plastique","goblet en papier","metal","carton","vide"],batch_size=371)
                
test_images, labels = next(test_batches)

model = keras.models.load_model('model3')


score = model.evaluate(test_images, labels, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# results = []
# for pred in predictions:
#   x = np.argmax(pred)
#   arr = [0.0]*7
#   arr[x] = 1.0
#   results.append(arr)

# results = np.array(results)

# cm = confusion_matrix(labels,results)

# cm_plot_labels = ["Bouteille","Plastique","goblet plastique","goblet en papier","metal","carton","vide"]

# def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
#     """
#     This function prints and plots the confusion matrix.
#     Normalization can be applied by setting `normalize=True`.
#     (This function is copied from the scikit docs.)
#     """
#     plt.figure()
#     plt.imshow(cm, interpolation='nearest', cmap=cmap)
#     plt.title(title)
#     plt.colorbar()
#     tick_marks = np.arange(len(classes))
#     plt.xticks(tick_marks, classes, rotation=45)
#     plt.yticks(tick_marks, classes)

#     if normalize:
#         cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
#     print(cm)
#     thresh = cm.max() / 2.
#     for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
#         plt.text(j, i, cm[i, j], horizontalalignment="center", color="white" if cm[i, j] > thresh else "black")

#     plt.tight_layout()
#     plt.ylabel('True label')
#     plt.xlabel('Predicted label')

# plot_confusion_matrix(cm,cm_plot_labels)