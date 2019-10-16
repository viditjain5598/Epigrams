from epigrams import Perilisms
import sys
from PyQt4 import QtGui
import random

ind = random.randrange(0, 120, 1)
#print("Epigram #{}\n".format(ind+1) + Perilisms[ind]) #debug statement

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()

window.resize(400, 240)
window.setWindowTitle('Epigrams')

txt = QtGui.QLabel("Perlis #{}\n\n".format(ind)+Perilisms[ind], window)
txt.setWordWrap(True)
txt.resize(370, 150)
txt.move(20, 30)

btn1 = QtGui.QPushButton('Exit!', window)
btn1.setToolTip('Click to quit!')
btn1.clicked.connect(exit)
btn1.resize(btn1.sizeHint())
btn1.move(40, 180)

btn2 = QtGui.QPushButton('Refresh!', window)
btn2.setToolTip('Click to Refresh!')
btn2.clicked.connect(exit)
btn2.resize(btn2.sizeHint())
btn2.move(160, 180)

window.show()

sys.exit(app.exec_())