from PyQt5.QtWidgets import QApplication,QPushButton,QLabel,QVBoxLayout,QHBoxLayout,QMainWindow,QWidget
import sys
from PyQt5.QtGui import QIcon,QFont,QPixmap

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.counter=0
        self.gamer1_point=0
        self.gamer2_point=0
        self.gamer1_1=False
        self.gamer2_1=False
        self.gamer1_2=False
        self.gamer2_2=False
        self.gamer1_3=False
        self.gamer2_3=False
        self.gamer1_4=False
        self.gamer2_4=False
        self.gamer1_5=False
        self.gamer2_5=False
        self.gamer1_6=False
        self.gamer2_6=False
        self.gamer1_7=False
        self.gamer2_7=False
        self.gamer1_8=False
        self.gamer2_8=False
        self.gamer1_9=False
        self.gamer2_9=False
        self.main()   
        
    def main(self):
        self.window2=QWidget()
        self.window2.setStyleSheet("Background :Black")
        self.window2.setWindowTitle("XOX GAME")
        self.window2.setMaximumSize(200,200)
        self.button=QPushButton("1")
        self.button2=QPushButton("2")
        self.button3=QPushButton("3")
        self.button4=QPushButton("4")
        self.button5=QPushButton("5")
        self.button6=QPushButton("6")
        self.button7=QPushButton("7")
        self.button8=QPushButton("8")
        self.button9=QPushButton("9")
        self.clear=QPushButton("Clear")
        self.finish=QPushButton("Finish")
        self.reset=QPushButton("Reset Score")
        
        self.button.setFont(QFont("Arial",14,4))
        self.button2.setFont(QFont("Arial",14,4))
        self.button3.setFont(QFont("Arial",14,4))
        self.button4.setFont(QFont("Arial",14,4))
        self.button5.setFont(QFont("Arial",14,4))
        self.button6.setFont(QFont("Arial",14,4))
        self.button7.setFont(QFont("Arial",14,4))
        self.button8.setFont(QFont("Arial",14,4))
        self.button9.setFont(QFont("Arial",14,4))
        self.clear.setFont(QFont("Arial",20,4))
        self.finish.setFont(QFont("Arial",20,4))
        self.reset.setFont(QFont("Arial",20,4))
        
        self.button.setFixedSize(100,100)
        self.button2.setFixedSize(100,100)
        self.button3.setFixedSize(100,100)
        self.button4.setFixedSize(100,100)
        self.button5.setFixedSize(100,100)
        self.button6.setFixedSize(100,100)
        self.button7.setFixedSize(100,100)
        self.button8.setFixedSize(100,100)
        self.button9.setFixedSize(100,100)
        
        self.button.setStyleSheet("background: white")
        self.button2.setStyleSheet("background: white")
        self.button3.setStyleSheet("background: white")
        self.button4.setStyleSheet("background: white")
        self.button5.setStyleSheet("background: white")
        self.button6.setStyleSheet("background: white")
        self.button7.setStyleSheet("background: white")
        self.button8.setStyleSheet("background: white")
        self.button9.setStyleSheet("background: white")
        self.clear.setStyleSheet("background: red")
        self.finish.setStyleSheet("background: Green")
        self.reset.setStyleSheet("background: Yellow")
        
        self.gamer1_main=QLabel(f"Player1's Point: {self.gamer1_point}")
        self.gamer2_main=QLabel(f"Player2's Point: {self.gamer2_point}")
        self.gamer1_main.setFont(QFont("Arial",20,4,True))
        self.gamer2_main.setFont(QFont("Arial",20,4,True))
        self.gamer1_main.setStyleSheet("color: Blue")
        self.gamer2_main.setStyleSheet("color : Red")
        
        h_box6=QHBoxLayout()
        h_box6.addSpacing(90)
        h_box6.addWidget(self.reset)
        h_box6.addSpacing(50)
        h_box6.addWidget(self.clear)
        h_box6.addSpacing(30)
        h_box6.addWidget(self.finish)
        h_box6.addSpacing(90)
        
        h_box5=QHBoxLayout()
        h_box5.addStretch()
        h_box5.addWidget(self.gamer1_main)
        h_box5.addSpacing(30)
        h_box5.addWidget(self.gamer2_main)
        h_box5.addStretch()
        
        h_box=QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.button)
        h_box.addSpacing(20)
        h_box.addWidget(self.button2)
        h_box.addSpacing(20)
        h_box.addWidget(self.button3)
        h_box.addStretch()
        
        h_box2=QHBoxLayout()
        h_box2.addStretch()
        h_box2.addWidget(self.button4)
        h_box2.addSpacing(20)
        h_box2.addWidget(self.button5)
        h_box2.addSpacing(20)
        h_box2.addWidget(self.button6)
        h_box2.addStretch()
        
        h_box3=QHBoxLayout()
        h_box3.addStretch()
        h_box3.addWidget(self.button7)
        h_box3.addSpacing(20)
        h_box3.addWidget(self.button8)
        h_box3.addSpacing(20)
        h_box3.addWidget(self.button9)
        h_box3.addStretch()
        
        v_box=QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(h_box5)
        v_box.addSpacing(20)
        v_box.addLayout(h_box)
        v_box.addSpacing(20)
        v_box.addLayout(h_box2)
        v_box.addSpacing(20)
        v_box.addLayout(h_box3)
        v_box.addSpacing(20)
        v_box.addLayout(h_box6)
        v_box.addStretch()
        self.window2.setLayout(v_box)
        
        self.button.clicked.connect(self.process)
        self.button2.clicked.connect(self.process)
        self.button3.clicked.connect(self.process)
        self.button4.clicked.connect(self.process)
        self.button5.clicked.connect(self.process)
        self.button6.clicked.connect(self.process)
        self.button7.clicked.connect(self.process)
        self.button8.clicked.connect(self.process)
        self.button9.clicked.connect(self.process)
        self.clear.clicked.connect(self.process)
        self.finish.clicked.connect(self.process)
        self.reset.clicked.connect(self.process)
        self.window2.show()
    
    def process(self):
      sender=self.window2.sender()
      self.counter +=1
      if sender.text()=="Finish":
        if (self.gamer1_1 and self.gamer1_2 and self.gamer1_3):
            self.gamer1_point +=1
            self.congratulations()
            
        elif (self.gamer1_4 and self.gamer1_5 and self.gamer1_6):
            self.gamer1_point+=1
            self.congratulations()
            
        elif (self.gamer1_7 and self.gamer1_8 and self.gamer1_9):
            self.gamer1_point+=1
            self.congratulations()
            
        elif (self.gamer1_1 and self.gamer1_4 and self.gamer1_7):
            self.gamer1_point +=1
            self.congratulations()
            
        elif (self.gamer1_2 and self.gamer1_5 and self.gamer1_8):
            self.gamer1_point +=1
            self.congratulations()
            
        elif (self.gamer1_3 and self.gamer1_6 and self.gamer1_9):
            self.gamer1_point +=1  
            self.congratulations()
            
        elif (self.gamer1_1 and self.gamer1_5 and self.gamer1_9):
            self.gamer1_point +=1
            self.congratulations()
            
        elif (self.gamer1_3 and self.gamer1_5 and self.gamer1_7):
            self.gamer1_point +=1
            self.congratulations()
            
        elif (self.gamer2_1 and self.gamer2_2 and self.gamer2_3):
            self.gamer2_point +=1
            self.congratulations()
            
        elif (self.gamer2_4 and self.gamer2_5 and self.gamer2_6):
            self.gamer2_point+=1
            self.congratulations()
            
        elif (self.gamer2_7 and self.gamer2_8 and self.gamer2_9):
            self.gamer2_point+=1
            self.congratulations()
            
        elif (self.gamer2_1 and self.gamer2_4 and self.gamer2_7):
            self.gamer2_point +=1
            self.congratulations()
            
        elif (self.gamer2_2 and self.gamer2_5 and self.gamer2_8):
            self.gamer2_point +=1
            self.congratulations()
            
        elif (self.gamer2_3 and self.gamer2_6 and self.gamer2_9):
            self.gamer2_point +=1  
            self.congratulations()
            
        elif (self.gamer2_1 and self.gamer2_5 and self.gamer2_9):
            self.gamer2_point +=1
            self.congratulations()
            
        elif (self.gamer2_3 and self.gamer2_5 and self.gamer2_7):
            self.gamer2_point +=1
            self.congratulations()
        
        else:
            self.counter=0
            self.button.setText("1")
            self.button2.setText("2")
            self.button3.setText("3")
            self.button4.setText("4")
            self.button5.setText("5")
            self.button6.setText("6")
            self.button7.setText("7")
            self.button8.setText("8")
            self.button9.setText("9")
        
            self.button.setStyleSheet("background: white")
            self.button2.setStyleSheet("background: white")
            self.button3.setStyleSheet("background: white")
            self.button4.setStyleSheet("background: white")
            self.button5.setStyleSheet("background: white")
            self.button6.setStyleSheet("background: white")
            self.button7.setStyleSheet("background: white")
            self.button8.setStyleSheet("background: white")
            self.button9.setStyleSheet("background: white")
            
            self.gamer1_1=False
            self.gamer2_1=False
            self.gamer1_2=False
            self.gamer2_2=False
            self.gamer1_3=False
            self.gamer2_3=False
            self.gamer1_4=False
            self.gamer2_4=False
            self.gamer1_5=False
            self.gamer2_5=False
            self.gamer1_6=False
            self.gamer2_6=False
            self.gamer1_7=False
            self.gamer2_7=False
            self.gamer1_8=False
            self.gamer2_8=False
            self.gamer1_9=False
            self.gamer2_9=False
            
      elif sender.text() =="1":
            
            if self.counter%2!=0:
              self.button.setStyleSheet("background:blue;color: green")
              self.button.setText("X")
              
              self.gamer1_1=True
            else:
              self.button.setStyleSheet("background:red")  
              self.button.setText("O")
              self.gamer2_1=True
            
            
      elif sender.text() =="2":
            
            if self.counter%2!=0:
              self.button2.setStyleSheet("background:blue;color: green")
              self.button2.setText("X")
            
              self.gamer1_2=True
            else:
              self.button2.setStyleSheet("background:red")  
              self.button2.setText("O")
              self.gamer2_2=True
            
            
      elif sender.text() =="3":
            
            if self.counter%2!=0:
              self.button3.setStyleSheet("background:blue;color: green")
              self.button3.setText("X")
              
              self.gamer1_3=True
            else:
              self.button3.setStyleSheet("background:red")  
              self.button3.setText("O")
              
              self.gamer2_3=True
            
            
      elif sender.text() =="4":
            
            if self.counter%2!=0:
              self.button4.setStyleSheet("background:blue;color: green")
              self.button4.setText("X")
             
              self.gamer1_4=True
            else:
              self.button4.setStyleSheet("background:red")  
              self.button4.setText("O")
              self.gamer2_4=True
            
        
      elif sender.text() =="5":
            
            if self.counter%2!=0:
              self.button5.setStyleSheet("background:blue;color: green")
              self.button5.setText("X")
              
              self.gamer1_5=True
            else:
              self.button5.setStyleSheet("background:red")  
              self.button5.setText("O")
              self.gamer2_5=True
            
        
      elif sender.text() =="6":
            
            if self.counter%2!=0:
              self.button6.setStyleSheet("background:blue;color: green")
              self.button6.setText("X")
      
              self.gamer1_6=True
            else:
              self.button6.setStyleSheet("background:red")  
              self.button6.setText("O")
              self.gamer2_6=True
            
            
      elif sender.text() =="7":
            
            if self.counter%2!=0:
              self.button7.setStyleSheet("background:blue; color: green")
              self.button7.setText("X")
              
              self.gamer1_7=True
            else:
              self.button7.setStyleSheet("background:red")  
              self.button7.setText("O")
              self.gamer2_7=True
            
            
      elif sender.text() =="8":
            
            if self.counter%2!=0:
              self.button8.setStyleSheet("background:blue;color: green")
              self.button8.setText("X")
              
              self.gamer1_8=True
            else:
              self.button8.setStyleSheet("background:red")  
              self.button8.setText("O")
              self.gamer2_8=True
            
            
      elif sender.text() =="9":
            
            if self.counter%2!=0:
              self.button9.setStyleSheet("background:blue;color: green")
              self.button9.setText("X")
          
              self.gamer1_9=True
            else:
              self.button9.setStyleSheet("background:red")  
              self.button9.setText("O")
              self.gamer2_9=True
            
      elif sender.text()=="Clear":
            self.counter=0
            self.button.setText("1")
            self.button2.setText("2")
            self.button3.setText("3")
            self.button4.setText("4")
            self.button5.setText("5")
            self.button6.setText("6")
            self.button7.setText("7")
            self.button8.setText("8")
            self.button9.setText("9")
        
            self.button.setStyleSheet("background: white")
            self.button2.setStyleSheet("background: white")
            self.button3.setStyleSheet("background: white")
            self.button4.setStyleSheet("background: white")
            self.button5.setStyleSheet("background: white")
            self.button6.setStyleSheet("background: white")
            self.button7.setStyleSheet("background: white")
            self.button8.setStyleSheet("background: white")
            self.button9.setStyleSheet("background: white")
            
            self.gamer1_1=False
            self.gamer2_1=False
            self.gamer1_2=False
            self.gamer2_2=False
            self.gamer1_3=False
            self.gamer2_3=False
            self.gamer1_4=False
            self.gamer2_4=False
            self.gamer1_5=False
            self.gamer2_5=False
            self.gamer1_6=False
            self.gamer2_6=False
            self.gamer1_7=False
            self.gamer2_7=False
            self.gamer1_8=False
            self.gamer2_8=False
            self.gamer1_9=False
            self.gamer2_9=False
      elif sender.text()=="Reset Score":
          self.gamer1_point=0
          self.gamer2_point=0
          self.gamer1_main.setText(f"Player1's Point: {self.gamer1_point}")
          self.gamer2_main.setText(f"Player2's Point: {self.gamer2_point}") 
          self.counter=0
          self.button.setText("1")
          self.button2.setText("2")
          self.button3.setText("3")
          self.button4.setText("4")
          self.button5.setText("5")
          self.button6.setText("6")
          self.button7.setText("7")
          self.button8.setText("8")
          self.button9.setText("9")
        
          self.button.setStyleSheet("background: white")
          self.button2.setStyleSheet("background: white")
          self.button3.setStyleSheet("background: white")
          self.button4.setStyleSheet("background: white")
          self.button5.setStyleSheet("background: white")
          self.button6.setStyleSheet("background: white")
          self.button7.setStyleSheet("background: white")
          self.button8.setStyleSheet("background: white")
          self.button9.setStyleSheet("background: white")
            
          self.gamer1_1=False
          self.gamer2_1=False
          self.gamer1_2=False
          self.gamer2_2=False
          self.gamer1_3=False
          self.gamer2_3=False
          self.gamer1_4=False
          self.gamer2_4=False
          self.gamer1_5=False
          self.gamer2_5=False
          self.gamer1_6=False
          self.gamer2_6=False
          self.gamer1_7=False
          self.gamer2_7=False
          self.gamer1_8=False
          self.gamer2_8=False
          self.gamer1_9=False
          self.gamer2_9=False
      else:
         self.counter -=1
    
    def congratulations(self):
        self.window1=QWidget()
        self.window1.setWindowTitle("XOX GAME")
        
        self.picture=QLabel()
        self.picture.setPixmap(QPixmap("Congrulation.jpeg"))
        v_box=QVBoxLayout()
        h_box=QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.picture)
        h_box.addStretch()
        
        v_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addStretch()
        
        self.window1.setLayout(v_box)
        self.gamer1_main.setText(f"Player1's Point: {self.gamer1_point}")
        self.gamer2_main.setText(f"Player2's Point: {self.gamer2_point}") 
        self.window1.setMaximumSize(200,200)
        
        self.window1.show()    
       
           
app=QApplication(sys.argv)
app.setWindowIcon(QIcon("XOX.png"))
App=Window()
sys.exit(app.exec())
        