import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore


class MyTable(QWidget):

    def __init__(self,dataset,title):
        super(MyTable, self).__init__()
        self.dataset=dataset
        self.title=title
        self.Table(self.dataset)

    def Table(self,dataset):
        self.mytable(dataset)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)
        #self.setWindowIcon(QtGui.QIcon(''))
        self.setGeometry(50,100,900,500)
        self.setWindowTitle(self.title)

        
        self.show()
        
        

    def mytable(self,data):
        
        self.tableWidget = QTableWidget()
        self.data=data
        self.tableWidget.setRowCount(len(self.data))
        self.tableWidget.setColumnCount(len(self.data[0]))
        
        


        for i in range(0,len(self.data)):
            for j in range(0,len(self.data[0])):
                self.tableWidget.setItem(i, j , QTableWidgetItem(str(self.data[i][j])))
                
          
def Main(dataset,title):
   
    if not QApplication.instance():
        app =QApplication(sys.argv)
    else:
        app = QApplication.instance() 
       

    #qapplication_constructor = QApplication(sys.argv)
    gui = MyTable(dataset,title)
    gui.exit(app.exec_())
    #app.deleteLater(qapplication_constructor.exec_())
    
    
  

