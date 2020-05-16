import sys
from PyQt5.QtWidgets import QApplication
from weath import weather_window

app = QApplication(sys.argv)

weatherapp = weather_window()

sys.exit(app.exec_())