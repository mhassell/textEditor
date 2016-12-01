import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        
        super(Window,self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle('PyQt Tutorial')
        self.setWindowIcon(QtGui.QIcon('favicon.png'))

        # add an exit feature
        extractAction = QtGui.QAction('&Close', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('Leave the App')
        extractAction.triggered.connect(self.close_application)
        
        # add a text editor window
        openEditor = QtGui.QAction('&Editor',self)
        openEditor.setShortcut('Crtl+E')
        openEditor.setStatusTip('Open Editor')
        openEditor.triggered.connect(self.editor)

        # open files to edit in the editor
        openFile = QtGui.QAction('&Open file',self)
        openFile.setShortcut('Crtl+O')
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)

        # save files to edit in the editor
        saveFile = QtGui.QAction('&Save file',self)
        saveFile.setShortcut('Crtl+S')
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)

        self.statusBar()

        # menu part of exit feature
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        # add the editor to the menu
        editorMenu  = mainMenu.addMenu('&Editor')
        editorMenu.addAction(openEditor)
        editorMenu.addAction(openFile)

        # add the save to the menu
        editorMenu.addAction(saveFile)

        self.home()

    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name,'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name, 'r')

        self.editor()

        with file:
            text = file.read()
            self.textEdit.setText(text)

    def home(self):
        self.show()

    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)

    def close_application(self):
        # add functionality to see if we want to exit
        choice = QtGui.QMessageBox.question(self,'Exit','Are you sure you want to exit?',
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.Yes:
            print('Exiting')
            sys.exit()
        else:
            pass

def run(): 
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()

