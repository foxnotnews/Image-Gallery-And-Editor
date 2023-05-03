from PyQt5.QtWidgets import QApplication,QFileDialog,QMainWindow
import os
import xml.etree.ElementTree as xml
import sys
from PyQt5.QtGui import QPixmap
from GUI_design import*
from screeninfo import get_monitors


FILES=[]
image_type=(".png" ,".jpg", ".jpeg", ".bmp")




class Application(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_dialog=QFileDialog()
        
        #select specific files selected
        self.files_selected=[]
        
        self.actionLoad_FIles.triggered.connect(self.select_files)
        self.actionLoad_Folder.triggered.connect(self.Load_folder)
        self.current_image=0
        self.previous_image_button.clicked.connect(self.previous_image)
        self.next_image_button.clicked.connect(self.next_image)
        self.Save.clicked.connect(self.reset_image_displayed)
        self.Select_button.clicked.connect(self.selected_image)

    #load folder/but only images
    def Load_folder(self) :
        self.directory = str(QtWidgets.QFileDialog.getExistingDirectory())
        self.files=os.listdir(f"{self.directory}")
        
        for file in self.files:
            if file.endswith(image_type):
                FILES.append(f"{self.directory}/{file}")
        print(FILES)
        self.current_display_image()


        

    def selected_image(self):
        image_path=FILES[self.current_image]
        self.files_selected.append(image_path)
        print(self.files_selected)
    

    def reset_image_displayed(self):
        FILES=self.files_selected
        self.current_display_image()
        print(FILES)
        

    #select 1/ multiple iamge to put in the list FILES
    def select_files(self):
        #file method
        self.load_dialog.setFileMode(QFileDialog.ExistingFiles)
        self.load_dialog.setNameFilter(f"Image files *.png *.jpg *.jpeg *.bmp")
        if self.load_dialog.exec_():
            filenames = self.load_dialog.selectedFiles()
            for file in filenames:
                if file not in FILES:
                    FILES.append(file)
            print(FILES)
                    
            self.current_display_image()          
    #display the image on GUI
    def current_display_image(self):
        resolution = self.__get_screen_resolution()
        if len(FILES)!=0 or self.current_image< len(FILES):
            self.pixmap = QPixmap(FILES[self.current_image]).scaled(int(resolution[0]*0.8), int(resolution[1]*0.8))
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
    def __get_screen_resolution(self): 
        #returns the resolution of the main monitor
        #
        #Input: -
        #
        #Output: a list containing the width and height of the primary system monitor.
        for monitor in get_monitors():
            if(monitor.is_primary):
                width = monitor.width
                height = monitor.height
        assert width > 0, f"screen width > 0 expected, got: {width}"
        assert height > 0, f"screen width > 0 expected, got: {height}"
        return([width, height])

        



app=QApplication(sys.argv)
window=Application()

window.show()
app.exec()
