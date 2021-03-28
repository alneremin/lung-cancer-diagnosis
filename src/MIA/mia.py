
import keras, os
from keras.preprocessing import image
from keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np

import logging

logger = logging.getLogger('log02')

class MIA:

    def __init__(self, path):
        self.path = path
        self.model = None
        self.categories = ['A', 'B', 'E', 'G']
        self.work = False 

    def loadModel(self):
        if self.model is None:
            try:
                self.model = load_model(self.path)
                return True
            except Exception as e:
                logger.exception('Не удалось загрузить модель нейросети')
                return False
        return True

    def classify(self, img):
        lung = None
        try:
            lung = image.load_img(img,target_size=(224,224))
        except Exception as e:
            logger.exception('Не удалось загрузить КТ-снимок')
            return False, ''
        lung = np.asarray(lung)
        #plt.imshow(lung)
        lung = np.expand_dims(lung, axis=0)
        pred = self.model.predict(lung)
        logger.info(f"Результаты анализа: {pred[0]}")
        return True, self.categories[np.argmax(pred[0])]
        #print([round(i) for i in output[0]])