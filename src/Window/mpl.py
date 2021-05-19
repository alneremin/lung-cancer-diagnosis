# Imports
from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib.image as mpimg
import SimpleITK as sitk
import numpy as np
import os
from scipy import stats
import matplotlib.pylab as pylab
import matplotlib

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')

# Matplotlib canvas class to create figure
class MplCanvas(Canvas):
    def __init__(self):
        self.fig = Figure(figsize=(30,20))
        #self.axes = self.fig.subplots(nrows=1, ncols=2)
        #self.axes[0].set(title = 'Исходный КТ-снимок')
        #self.axes[0].set(title = 'Сегментированный КТ-снимок')
        #self.axes[1].set(title = 'Класс опухоли: неизвестен')
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)

    def draw_img(self, result):

        if len(result) < 1: return

        nrows = len(result) // 5 + 1
        ncols = len(result) if len(result) < 6 else 5
        self.axes = self.fig.subplots(nrows=nrows, ncols=ncols)#s, sharex=True, sharey=True, subplot_kw=dict(frameon=False))
        matplotlib.pyplot.subplots_adjust(wspace=.0,hspace=0.)

        mode = stats.mode([i.imgClass for i in result])[0][0]
        self.fig.suptitle('Класс опухоли: ' + mode, fontsize=16)

        params = {'axes.labelsize': 4, 'axes.titlesize':4 }
        pylab.rcParams.update(params)

        rez_len = len(result) - 1
        for i in range(nrows):
            for j in range(ncols):
                if rez_len < 0: return
                lung = sitk.GetArrayFromImage(sitk.ReadImage(result[rez_len].pathToInitImg))
                lung = lung.reshape((512,512))#.astype(np.uint8)

                #img = mpimg.imread(pathToInputFile)
                #self.axes[0].imshow(lung)
                #self.axes[i][j].imshow(result[rez_len].segmentatedImg)
                if nrows == 1:
                    axesj = self.axes
                else:
                    axesj = self.axes[i]
                #axesj[j].set(title = os.path.split(result[rez_len].pathToInitImg)[1][:-4])
                axesj[j].imshow(lung)
                
                y1, x1, y2, x2 = result[rez_len].tumorBorders * 512
                color = np.array([219, 57, 57]) / 255
                p = matplotlib.patches.Rectangle((x1, y1), x2 - x1, y2 - y1, linewidth=2,
                                        alpha=0.7, linestyle="solid",
                                        edgecolor=color, facecolor='none')
                axesj[j].add_patch(p)
                rez_len -= 1
        self.draw()