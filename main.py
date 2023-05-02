from PyQt5.QtWidgets import QApplication,QFileDialog,QMainWindow
import subprocess
import xml.etree.ElementTree as xml
import sys
from PyQt5.QtWidgets import QApplication,QFileDialog,QMainWindow
from PyQt5.QtGui import QPixmap
from GUI_design import*


FILES=[]
image_type="(*.png *.jpg *.jpeg *.bmp)"




class Application(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #File load method
        self.load_dialog=QFileDialog()
        self.load_dialog.setFileMode(QFileDialog.ExistingFiles)
        self.load_dialog.setNameFilter(f"Image files {image_type}")
        self.load_image_button.clicked.connect(self.select_files)
        self.current_image=0
        self.previous_image_button.clicked.connect(self.previous_image)
        self.next_image_button.clicked.connect(self.next_image)            

    #select 1/ multiple iamge to put in the list FILES
    def select_files(self):
        if self.load_dialog.exec_():
            filenames = self.load_dialog.selectedFiles()
            for file in filenames:
                if file not in FILES:
                    FILES.append(file)
            print(FILES)
                    
            self.current_display_image()          
    #display the image on GUI
    def current_display_image(self):
       
        if len(FILES)!=0 or self.current_image< len(FILES):
            self.pixmap = QPixmap(FILES[self.current_image])
            self.display_image.setPixmap(self.pixmap)
    #go to next image on the list FILES
    def next_image(self):
        if len(FILES)==0 or self.current_image>len(FILES) or self.current_image==len(FILES)-1:
            return 0
        else:
            self.current_image+=1
            self.current_display_image()
    #go to the previous image on the list FILES
    def previous_image(self):
        if len(FILES)== 0 or self.current_image>len(FILES) or self.current_image==0:
            return 0
        else:
            self.current_image -=1
            self.current_display_image()
    

        



app=QApplication(sys.argv)
window=Application()

window.show()
app.exec()
