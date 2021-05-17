# Imports
from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib.image as mpimg
import SimpleITK as sitk
import matplotlib

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')

# Matplotlib canvas class to create figure
class MplCanvas(Canvas):
    def __init__(self):
        self.fig = Figure(figsize=(15,12))
        self.ax = self.fig.add_subplot(121)
        self.ax.set(title = 'Исходный КТ-снимок')
        self.ax2 = self.fig.add_subplot(122)
        self.ax2.set(title = 'Сегментированный КТ-снимок')
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)

    def draw_img(self, pathToInputFile, segmImage):

        lung = sitk.GetArrayFromImage(sitk.ReadImage(pathToInputFile))
        lung = lung.reshape((512,512))#.astype(np.uint8)

        #img = mpimg.imread(pathToInputFile)
        self.ax.imshow(lung)
        self.ax2.imshow(segmImage)
        self.draw()