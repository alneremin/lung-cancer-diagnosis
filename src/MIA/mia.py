
import keras, os
from keras.preprocessing import image
from keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import SimpleITK as sitk
from lungmask import mask

import logging

logger = logging.getLogger('log02')

class MIA:

    def __init__(self, path):
        self.path = path
        self.model = dict()
        self.categories = ['A', 'B', 'E', 'G']
        self.types = ['segment', 'class']
        self.work = False 

    def loadClassificationModel(self):
        if 'class' not in self.model.keys():
            try:
                self.model['class'] = load_model(self.path['class'])
                return True
            except Exception as e:
                logger.exception('Не удалось загрузить модель нейросети')
                return False
        return True

    def loadSegmentationModel(self):
        if 'segment' not in self.model.keys():
            try:
                self.model['segment'] = mask.get_model('unet','LTRCLobes')
                return True
            except Exception as e:
                logger.exception('Не удалось загрузить модель нейросети')
                return False
        return True

    def classify(self, img, _format='dcm'):
        if _format=="jpg":
            lung = None
            try:
                lung = image.load_img(img,target_size=(224,224))
            except Exception as e:
                logger.exception('Не удалось загрузить КТ-снимок')
                return False, ''
            lung = np.asarray(lung)
            #plt.imshow(lung)
            lung = np.expand_dims(lung, axis=0)
        else:
            lung = None
            try:
                lung = sitk.GetArrayFromImage(sitk.ReadImage(img))
                lung = lung.reshape((512,512)).astype(np.uint8)
                pil_img = Image.fromarray(lung, 'L')
                pil_img.thumbnail((224,224), Image.ANTIALIAS)
                lung = np.asarray(pil_img)
                #lung = np.stack((lung,)*3, axis=-1)
                lung = np.expand_dims(lung, axis=0)
                print(lung.shape)
            except Exception as e:
                logger.exception('Не удалось загрузить КТ-снимок')
                return False, ''

        pred = self.model['class'].predict(lung)
        logger.info(f"Результаты анализа: {pred}")
        return True, self.categories[np.argmax(pred[1])], pred[0][0]
        #print([round(i) for i in output[0]])

    def segmentify(self, img):
        lung = None
        try:
            lung = sitk.ReadImage(img)
            is_ct = str.strip(lung.GetMetaData("0028|0004")) == "MONOCHROME2"
        
            if not is_ct:
                print(img, "is not MONOCHROME2")
                raise Exception(img + " is not MONOCHROME2")
        except Exception as e:
            logger.exception('Не удалось загрузить КТ-снимок')
            return False, [], ''

        pred = mask.apply(lung, self.model['segment'])
        logger.info(f"Результаты анализа: image")

        new_path = img[:-4] + "_segmentated.dcm"
        writer = sitk.ImageFileWriter()
        writer.SetFileName(new_path)
        writer.Execute(sitk.GetImageFromArray(pred))
        print(new_path, "is saved.")

        return True, pred.reshape((512,512)), new_path