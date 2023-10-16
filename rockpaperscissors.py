'''
Made by Marian Mendoza
Playing around with GUI PYQT
Trying to implement a Rock, paper scissors game


'''



import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget, QMessageBox
from PyQt5.QtCore import Qt


class RPS(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Window
        self.choice = ""
        self.setWindowTitle("Rock Paper Scissors")
        self.setGeometry(100,100,400,400)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)



        # Label Layout
        self.layout = QVBoxLayout()

        # Label Layout Horizontol

        # Labels
        self.label = QLabel("Rock, Paper or Scissors?")
        self.layout.addWidget(self.label)

        # Label Results
        self.resultLabel = QLabel()
        self.resultLabel.setText("Select Weapon")
        self.resultLabel.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.resultLabel)


        # Label Enemy Weapon
        self.enemyLabel = QLabel()
        self.layout.addWidget(self.enemyLabel)

    
         # Label Player Weapon
        self.playerLabel = QLabel()
        self.layout.addWidget(self.playerLabel)

        
        
    # Display Rock
        self.rockButton = QPushButton("Rock", self)
        self.rockButton.setStyleSheet('background-color: #3498db; color: white; border: none;')
        self.layout.addWidget(self.rockButton)
       
    # Display Paper
        self.PaperButton = QPushButton("Paper", self)
        self.PaperButton.setStyleSheet('background-color: #3498db; color: white; border: none;')
        self.layout.addWidget(self.PaperButton)
        
        
    # Display Scissors
        self.ScissorButton = QPushButton("Scissors",self)
        self.ScissorButton.setStyleSheet('background-color: #3498db; color: white; border: none;')
        self.layout.addWidget(self.ScissorButton)
        central_widget.setLayout(self.layout)


        
        self.rockButton.clicked.connect(self.b1)
        self.PaperButton.clicked.connect(self.b2)
        self.ScissorButton.clicked.connect(self.b3)

# Pick Enemy Weapon
# Compare Weapons



    def b1(self):
        self.playerChoice = "Rock"
        self.playerLabel.setText(self.playerChoice)

        # print("Button Clicked! Rock")
        self.random_num = None
        self.pickEnemyWeapon()
        self.compareWeapons()

        


    def b2(self):
        self.playerChoice = "Paper"
        self.playerLabel.setText(self.playerChoice)

        # print("Button Clicked! Paper")
        self.random_num = None
        self.pickEnemyWeapon()
        self.compareWeapons()




    def b3(self):
        self.playerChoice = "Scissors"
        self.playerLabel.setText(self.playerChoice)
        # print("Button Clicked! Scissors")
        self.random_num = None
        self.pickEnemyWeapon()
        self.compareWeapons()




    def pickEnemyWeapon(self):
        
        self.enemy = ["Rock","Paper","Scissors"]
        self.random_num = random.randint(0,2)
        # print(self.random_num)
        for i in self.enemy:
            self.enemyChoice = self.enemy[self.random_num]
            self.enemyLabel.setText(self.enemyChoice)
            # print(self.enemyChoice)
            return self.enemyChoice
        
    def compareWeapons(self):
        winningCombo = {"Rock":"Scissors","Paper":"Rock","Scissors":"Paper"}
        for i , j in winningCombo.items():
            # print(i, j)
            # print("Player",self.playerChoice)
            # print("Enemy",self.enemyChoice)
            
            # If there is a tie
            if self.playerChoice == self.enemyChoice:
                self.tie()
                break
    
            # Win
            if i == self.playerChoice:
                if j == self.enemyChoice:
                    self.win()
                    break
                # Lose
                else:
                    self.lose()
                    break

    def lose(self):
        # Labels
        self.resultLabel.setText("You Lose!")
        self.resultLabel.setAlignment(Qt.AlignCenter)
        # print("You Lose!")


    def win(self):
        self.resultLabel.setText("You Win!")
        self.resultLabel.setAlignment(Qt.AlignCenter)
        # print("You Win!")
    

    def tie(self):
        self.resultLabel.setText("You Tie!")
        self.resultLabel.setAlignment(Qt.AlignCenter)
        # print("Tie")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RPS()
    window.show()
    sys.exit(app.exec_())