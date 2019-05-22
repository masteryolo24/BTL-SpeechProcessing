from PyQt5.QtWidgets import QDialog,QApplication ,QMessageBox, QListWidget, QCheckBox ,QComboBox, QGroupBox ,QDialogButtonBox , QVBoxLayout , QFrame,QTabWidget, QWidget, QLabel, QLineEdit, QPushButton
import sys
from PyQt5.QtCore import QFileInfo
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import s2i

class TabDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tab Widget Application")
        self.setWindowIcon(QIcon("myicon.png"))



        tabwidget = QTabWidget()
        tabwidget.addTab(FirstTab(), "First Tab")
        tabwidget.addTab(TabTwo(), "Second Tab")
        tabwidget.addTab(TabThree(), "Third Tab")


        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)

        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(tabwidget)

        vboxLayout.addWidget(buttonbox)

        self.setLayout(vboxLayout)

class FirstTab(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
        
        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20,80)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")


class TabTwo(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(100,70)
        button.clicked.connect(self.on_click)

        """ear
        button2 = QPushButton("Press to record", self)
        button2.setToolTip("test")
        button2.move(100, 100)
        button2.click.connect(self.onl)"""
        
        self.show()

    @pyqtSlot()
    def on_click(self):
        s2i.test()




class TabThree(QWidget):
    def __init__(self):
        super().__init__()


        label = QLabel("Terms And Conditions")
        listWidget = QListWidget()
        list = []

        for i in range(1,20):
            list.append("This Is Terms And Condition")

        listWidget.insertItems(0, list)
        checkBox = QCheckBox("Check The Terms And Conditions")


        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(listWidget)
        layout.addWidget(checkBox)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tabdialog = TabDialog()
    tabdialog.show()
    app.exec()