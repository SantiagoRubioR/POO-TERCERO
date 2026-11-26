import  sys
from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
ventana = QMainWindow()
ventana.setWindowTitle("Ventana Cooperativa")
ventana.resize(1200,800)
ventana.show()
sys.exit(app.exec())