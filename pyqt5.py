from PyQt5.QtWidgets import QDialog,QApplication , QListWidget, QCheckBox ,QComboBox, QGroupBox ,QDialogButtonBox , QVBoxLayout , QFrame,QTabWidget, QWidget, QLabel, QLineEdit
import sys
from PyQt5.QtCore import QFileInfo
from PyQt5.QtGui import QIcon



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

        filenameLabel = QLabel("Name:")
        fileNameEdit = QLineEdit()

        dob = QLabel("Birth Date:")
        dobedit = QLineEdit()

        age = QLabel("Age:")
        ageedit = QLineEdit()

        PhoneNu = QLabel("Phone:")
        phonedit = QLineEdit()

        ftablayout = QVBoxLayout()
        ftablayout.addWidget(filenameLabel)
        ftablayout.addWidget(fileNameEdit)
        ftablayout.addWidget(dob)
        ftablayout.addWidget(dobedit)
        ftablayout.addWidget(age)
        ftablayout.addWidget(ageedit)
        ftablayout.addWidget(PhoneNu)
        ftablayout.addWidget(phonedit)



        self.setLayout(ftablayout)


class TabTwo(QWidget):
    def __init__(self):
        super().__init__()

        selecGroup = QGroupBox("Select Operating System")
        combo = QComboBox()
        list = ["Windows", "Linux", "Fedora", "Kali", "Mac"]
        combo.addItems(list)
        selectLayout = QVBoxLayout()
        selectLayout.addWidget(combo)
        selecGroup.setLayout(selectLayout)


        checkGroup = QGroupBox("Which Operating System You Like ?")
        windows = QCheckBox("Windows")
        mac = QCheckBox("Mac")
        linux = QCheckBox("Linux")

        checkLayout = QVBoxLayout()
        checkLayout.addWidget(windows)
        checkLayout.addWidget(mac)
        checkLayout.addWidget(linux)
        checkGroup.setLayout(checkLayout)


        mainLayout = QVBoxLayout()
        mainLayout.addWidget(selecGroup)
        mainLayout.addWidget(checkGroup)
        self.setLayout(mainLayout)




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