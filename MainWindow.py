import sys

from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QProgressBar, QWidget, QCalendarWidget, QLCDNumber, QLabel, \
    QPushButton, QLineEdit, QCheckBox, QSpinBox, QSlider


class MainWindow(QMainWindow):

    # Le constructeur de la classe nous permet de changer quelques caractéristiques.
    def __init__(self):
        # Appel au constructeur parent (QMainWindow).
        super().__init__()
        # On change le titre de la fenêtre.
        self.setWindowTitle("Ma première fenêtre Qt avec Python")
        # On change l'icône affichée dans le bandeau supérieur de la fenêtre.
        self.setWindowIcon(QIcon("icons/yes.png"))
        # On retaille la fenêtre (800 pixels de large et 600 en hauteur).
        self.resize(800, 600)

        self.setMaximumSize(1024, 768)
        self.setToolTip("Hello World")

        # Le type QWidget représente un conteneur de widgets (et il est lui-même un widget).
        # On crée une instance que l'on va mettre au centre de la fenêtre.
        centralArea = QWidget()
        # On lui met une couleur d'arrière-plan, histoire de bien le voir.
        #  centralArea.setStyleSheet("background: #419eee")
        # On injecte ce widget en tant que zone centrale.
        self.setCentralWidget(centralArea)

        # On place maintenant chacun des composants souhaités dans la zone centrale.
        calendar = QCalendarWidget(centralArea)
        calendar.setGeometry(10, 10, 300, 200)

        lcd = QLCDNumber(self)
        lcd.display(1234)
        lcd.setGeometry(10, 220, 300, 70)

        label = QLabel("This is a label", centralArea)
        label.setGeometry(320, 10, 270, 30)

        button = QPushButton("This is a button", centralArea)
        button.setGeometry(320, 50, 270, 30)

        textBox = QLineEdit("This is a text box", centralArea)
        textBox.setGeometry(320, 90, 270, 30)

        checkBox = QCheckBox("This is a check box", centralArea)
        checkBox.setGeometry(320, 130, 270, 30)

        spinBox = QSpinBox(centralArea)
        spinBox.setValue(50)
        spinBox.setGeometry(320, 170, 270, 30)

        slider = QSlider(Qt.Horizontal, centralArea)
        slider.setValue(50)
        slider.setGeometry(320, 220, 270, 30)

        progress = QProgressBar(centralArea)
        progress.setValue(50)
        progress.setGeometry(320, 260, 270, 30)

        # Récupèration la barre de status
        statusBar = self.statusBar()
        statusBar.showMessage("This is my status bar")


if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication(sys.argv)

    # Instancier et afficher votre fenêtre graphique.
    window = MainWindow()
    window.show()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())