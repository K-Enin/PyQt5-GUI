#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 22:47:39 2021

"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os 
import shutil

path = os.path.dirname(__file__) 

class Window1(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Initialize Window
        self.setWindowTitle('Animal Scrollable Window')
        self.setFixedSize(800,600)
        
        self.scrollArea = QScrollArea(widgetResizable = True)
        self.setCentralWidget(self.scrollArea)
        content_widget = QWidget()
        self.scrollArea.setWidget(content_widget)
        self.layout = QVBoxLayout(content_widget)
    
        # Display images
        global IMAGES
        IMAGES = [f for f in os.listdir(path) if os.path.splitext(f)[-1]=='.png']
        
        global IMAGE_SIZE
        IMAGE_SIZE = len(IMAGES)
        
        self.ComboBoxes = dict()
        for i, single_images in enumerate(IMAGES):
            pixmap = QPixmap(path + '/' + single_images)
            pixmap = pixmap.scaled(770, 600, Qt.KeepAspectRatio, Qt.FastTransformation)
            label = QLabel(pixmap = pixmap)
            
            self.ComboBoxes[i] = QComboBox(self)
            animals = ['Cat', 'Dog', 'Rabbit', 'Undefined']
            self.ComboBoxes[i].addItems(animals)
            self.layout.addWidget(label)
            self.layout.addWidget(self.ComboBoxes[i])
        
        button_evaluate = QPushButton('Evaluate')
        self.layout.addWidget(button_evaluate)
        
        self.show()
        button_evaluate.pressed.connect(self.evaluate)
     
    def evaluate(self):
        for i in range(IMAGE_SIZE):
            currentText = self.ComboBoxes[i].currentText()
            os.makedirs(path + '/' + currentText)
            shutil.move(path + '/' + IMAGES[i], path + '/' + currentText + '/' + IMAGES[i])
        sys.exit()

def main():
    app = QApplication(sys.argv)
    window1 = Window1()
    sys.exit(app.exec_())
    
if __name__=='__main__':
    main()

