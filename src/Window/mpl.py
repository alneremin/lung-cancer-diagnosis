# Imports
from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib.image as mpimg
import SimpleITK as sitk
import numpy as np
import matplotlib

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')

# Matplotlib canvas class to create figure
class MplCanvas(Canvas):
    def __init__(self):
        self.fig = Figure(figsize=(15,12))
        self.axes = self.fig.subplots(nrows=1, ncols=2)

        #self.axes[0].set(title = 'Исходный КТ-снимок')
        self.axes[0].set(title = 'Сегментированный КТ-снимок')
        self.axes[1].set(title = 'Класс опухоли: неизвестен')
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)

    def draw_img(self, pathToInputFile, data):

        lung = sitk.GetArrayFromImage(sitk.ReadImage(pathToInputFile))
        lung = lung.reshape((512,512))#.astype(np.uint8)

        #img = mpimg.imread(pathToInputFile)
        #self.axes[0].imshow(lung)
        imgClass, segmentatedImg, tumorBorders = data
        self.axes[0].imshow(segmentatedImg)

        self.axes[1].set(title = 'Класс опухоли ' + imgClass)
        self.axes[1].imshow(lung)
        y1, x1, y2, x2 = tumorBorders * 512
        color = np.array([219, 57, 57]) / 255
        p = matplotlib.patches.Rectangle((x1, y1), x2 - x1, y2 - y1, linewidth=2,
                                alpha=0.7, linestyle="solid",
                                edgecolor=color, facecolor='none')
        self.axes[1].add_patch(p)

        self.draw()