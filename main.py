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
     QCheckBox,
)

def movefiles(sourcedir,destdir,count,convention, excn5, excomezarr):
    alldestinations = []
    alldestpaths = []
    unfound = []
    exclude = []
    if excn5:
        exclude.append('.n5')
    if excomezarr:
        exclude.append('.ome.zarr')
    for dirpath, dirnames, files in os.walk(destdir, topdown=True):
        dirnames[:] = [d for d in dirnames if d not in exclude]
        if os.path.isdir(os.path.join(dirpath)):
            print(f"Found {dirpath}")
            alldestpaths.append(dirpath)
            alldestinations.append(os.path.basename(dirpath))

    for file in os.listdir(sourcedir):
        standard = file[0:count]
        foldername = standard+convention
        if foldername in alldestinations:
            print(f"Moving {file} to {foldername}")
            if os.path.exists(os.path.join(alldestpaths[alldestinations.index(foldername)], file)):
                shutil.copy(os.path.join(sourcedir, file), os.path.join(sourcedir, file.split(".")[0]+'_copy'+ file.strip(file.split(".")[0])+file[-1]))
                shutil.copy(os.path.join(sourcedir, file.split(".")[0]+'_copy'+ file.strip(file.split(".")[0])+file[-1]), alldestpaths[alldestinations.index(foldername)])
                continue
            shutil.copy(os.path.join(sourcedir, file), alldestpaths[alldestinations.index(foldername)])
        else:
            print(f"Destination folder for {file} not found")
            unfound.append(file)

    return unfound

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Mover")
        self.source = "/"
        self.dest = os.getcwd()
        
        self.setLayout(self.mainwindow())

    def mainwindow(self):
        layout = QFormLayout()
        excn5 = True
        excomezarr = True

        def selectsourcefolder():
            self.source = QFileDialog.getExistingDirectory(self, 'Select Source Folder')

        def selectdestfolder():
            self.dest = QFileDialog.getExistingDirectory(self, 'Select Destination Folder')

        def checkn5(self):
            if excn5check.isChecked():
                excn5 = True
            else:
                excn5 = False

        def checkomezarr(self):
            if excomezarrcheck.isChecked():
                excomezarr = True
            else:
                excomezarr = False

        def move():
            unfound = movefiles(self.source, self.dest, int(get_count.text()), get_convention.text(), excn5, excomezarr)

            if len(unfound) > 0:
                errorlabel = QLabel()
                errorlabel.setText('The following files corresponding folders were not found:')
                layout.addRow(errorlabel)
                for i in unfound:
                    filelabel = QLabel()
                    filelabel.setText(i)
                    layout.addRow(filelabel)
            else:
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

        checklayout = QHBoxLayout()
        excn5check = QCheckBox(text='Exclude n5 files?')
        excn5check.setChecked(True)
        excn5check.stateChanged.connect(checkn5)
        checklayout.addWidget(excn5check)
        excomezarrcheck = QCheckBox(text='Exclude ome-zarr files?')
        excomezarrcheck.setChecked(True)
        excomezarrcheck.stateChanged.connect(checkomezarr)
        checklayout.addWidget(excomezarrcheck)

        finishbtn = QPushButton()
        finishbtn.setText('Move Files')
        finishbtn.clicked.connect(move)

        layout.addRow("Select source folder", sourcebtn)
        layout.addRow("Select destination folder", destbtn)
        layout.addRow("No. of similar chars between file and destination name:",get_count)
        layout.addRow("Destination name after the similar chars:",get_convention)
        layout.addRow(checklayout)
        layout.addRow(finishbtn)

        return layout

if __name__=='__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec_())
