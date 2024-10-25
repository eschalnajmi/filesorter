import sys
import os
import shutil
from PyQt5.QtWidgets import(
     QApplication, 
     QFileDialog, 
     QFormLayout, 
     QHBoxLayout,
     QWidget,
     QPushButton,
     QLineEdit,
     QLabel,
)

def movefiles(sourcedir,destdir,count,convention):
    alldestinations = []

    for d in os.listdir(destdir):
        if os.path.isdir(os.path.join(destdir, d)):
            alldestinations.append(d)

    for file in os.listdir(sourcedir):
        standard = file[0:count]
        foldername = standard+convention
        if foldername in alldestinations:
            shutil.copy(os.path.join(sourcedir, file), os.path.join(destdir, foldername, file))
        else:
            os.mkdir(os.path.join(destdir, foldername))
            alldestinations.append(foldername)
            shutil.copy(os.path.join(sourcedir, file), os.path.join(destdir, foldername, file))

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Mover")
        self.source = "/"
        self.dest = os.getcwd()
        
        self.setLayout(self.mainwindow())

    def mainwindow(self):
        layout = QFormLayout()

        def selectsourcefolder():
            self.source = QFileDialog.getExistingDirectory(self, 'Select Source Folder')

        def selectdestfolder():
            self.dest = QFileDialog.getExistingDirectory(self, 'Select Destination Folder')

        def move():
            movefiles(self.source, self.dest, int(get_count.text()), get_convention.text())
            exit(0)
        
        sourcelayout = QHBoxLayout()
        sourcebtn = QPushButton()
        sourcebtn.setText('Select Source Folder')
        sourcebtn.clicked.connect(selectsourcefolder)
        sourcedisplay = QLineEdit(f"{self.source}")
        sourcedisplay.setReadOnly(True)
        sourcelabel = QLabel()
        sourcelabel.setText('Source Folder:')
        sourcelayout.addWidget(sourcelabel)
        sourcelayout.addWidget(sourcedisplay)
        sourcelayout.addWidget(sourcebtn)

        destlayout = QHBoxLayout()
        destbtn = QPushButton()
        destbtn.setText('Select Destination Folder')
        destbtn.clicked.connect(selectdestfolder)
        destdisplay = QLineEdit(f"{self.dest}")
        destdisplay.setReadOnly(True)
        destlabel = QLabel()
        destlabel.setText('Destination Folder:')
        destlayout.addWidget(destlabel)
        destlayout.addWidget(destdisplay)
        destlayout.addWidget(destbtn)

        get_count = QLineEdit()
        get_convention = QLineEdit()

        finishbtn = QPushButton()
        finishbtn.setText('Move Files')
        finishbtn.clicked.connect(move)

        layout.addRow("Select source folder", sourcebtn)
        layout.addRow("Select destination folder", destbtn)
        layout.addRow("No. of similar chars between file and destination name:",get_count)
        layout.addRow("Destination name after the similar chars:",get_convention)
        layout.addRow(finishbtn)

        return layout
    
if __name__=='__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec_())