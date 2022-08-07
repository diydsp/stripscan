#!/usr/bin/env python3

import sys
import importlib

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import stscan_routines as sts

def reloadStsRoutines():
    importlib.reload( sts )

def buttonMake( win, text, pos, callback ):
    myButt = QPushButton( win )
    myButt.setText( text )
    myButt.move( pos['x'], pos['y'] )
    myButt.clicked.connect( callback )
    return myButt

def makeWindow():
    app = QApplication( sys.argv )
    win = QDialog()

    buttonList = []
    b1 = buttonMake( win, "reload", {'x':50,'y':20}, reloadStsRoutines )
    buttonList.append( b1 )
    b2 = buttonMake( win, "init", {'x':50,'y':70}, sts.init )
    buttonList.append( b2 )
    b3 = buttonMake( win, "step", {'x':50,'y':120}, sts.step )
    buttonList.append( b3 )
    

    win.setGeometry( 100, 100, 500, 300 )
    win.setWindowTitle( "STScan Dev" )
    win.show()
    sys.exit( app.exec_() )
                    
if __name__ == '__main__':
    makeWindow()

