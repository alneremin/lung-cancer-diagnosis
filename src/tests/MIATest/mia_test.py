
import sys
sys.path.insert(0, '../../')

import unittest
from MIA.mia import MIA
import logging

logger = logging.getLogger('log02')
logger.disabled = True

class TestMia(unittest.TestCase):

    modelPath = ""
    preparedImage = ""
    mia = MIA(modelPath)

    def testLoadModel(self):

        state = self.mia.loadModel()
        self.assertEqual(state, False)

        self.mia.path = self.modelPath
        print("Загрузка модуля...")
        state = self.mia.loadModel()
        self.assertEqual(state, True)

    def testСlassify(self):

        state, res = self.mia.classify('')
        self.assertEqual(state, False)

        state, res = self.mia.classify(self.preparedImage)

        self.assertEqual(state, True)
        self.assertEqual(res, 'A')


if __name__ == "__main__":
    
    TestMia.preparedImage = sys.argv.pop()
    TestMia.modelPath = sys.argv.pop()

    unittest.main()