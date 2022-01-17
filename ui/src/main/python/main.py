from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

path = '../../../../visualization/histogram.png'


def render():
    # Initialize application
    app = QApplication([])

    # Create label
    label = QLabel('Histogram')
    pixmap = QPixmap(path)
    label.setPixmap(pixmap)

    def refresh(event):
        pixmap = QPixmap(path)
        label.setPixmap(pixmap)

    # Create button
    button = QPushButton('Press me!')
    button.clicked.connect(refresh)

    # Create layout and add widgets
    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(button)

    # Apply layout to widget
    widget = QWidget()
    widget.setWindowTitle('Click Clock')
    widget.resize(1000, 750)
    widget.setLayout(layout)

    widget.show()

    app.exec_()


if __name__ == '__main__':
    render()
