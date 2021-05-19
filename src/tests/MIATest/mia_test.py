
import sys
sys.path.insert(0, '../../')

import unittest
from MIA.mia import MIA
import SimpleITK as sitk
from lungmask import mask

import logging

logger = logging.getLogger('log02')
logger.disabled = True


class TestClassifier(unittest.TestCase):

    modelPath = ""
    preparedImage = ""
    mia = MIA(dict())

    def testLoadClassificationModel(self):

        state = self.mia.loadClassificationModel()
        self.assertEqual(state, False)

        print(">", self.modelPath)
        self.mia.path['class'] = self.modelPath
        print("Загрузка модуля классификатора...")
        state = self.mia.loadClassificationModel()
        self.assertEqual(state, True)

    def testСlassify(self):

        state, res = self.mia.classify('')
        self.assertEqual(state, False)

        state, res = self.mia.classify(self.preparedImage)

        self.assertEqual(state, True)
        self.assertEqual(res, 'A')

class TestSegmenter(unittest.TestCase):

    preparedImage = ""
    mia = MIA(dict())

    def testLoadSegmentationModel(self):

        state = self.mia.loadSegmentationModel()
        self.assertEqual(state, True)

    def testSegmentify(self):

        state, res, _ = self.mia.segmentify('')
        self.assertEqual(state, False)

        state, res, _ = self.mia.segmentify(self.preparedImage)

        self.assertEqual(state, True)
        self.assertEqual(res.min(), 0)
        self.assertEqual(res.max(), 5)
        #self.assertEqual(res, 'A')


if __name__ == "__main__":
    
    
    TestClassifier.preparedImage = sys.argv.pop()
    TestClassifier.modelPath = sys.argv.pop()
    TestSegmenter.preparedImage = sys.argv.pop()

    unittest.main()


"""
 python3.7 mia_test.py \
 "/home/alner/documents/sem6/cource work/lung-cancer-diagnosis/src/tests/MIATest/1.3.6.1.4.1.14519.5.2.1.6655.2359.103293611003651848123608366756.dcm" \
 "/home/alner/Загрузки/vgg16_mia_model.h5" \
 "/home/alner/documents/sem6/cource work/lung-cancer-diagnosis/src/tests/MIATest/1.3.6.1.4.1.14519.5.2.1.6655.2359.103293611003651848123608366756_segmentated.dcm"
"""