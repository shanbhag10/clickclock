from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


def create_refresh_button():
    button = QPushButton('Refresh')
    button.setFixedWidth(80)
    button.setFixedHeight(30)
    button.setStyleSheet("""
            border: 3px solid black; 
            border-radius: 5px;
            background-color: #009be9;
            font-weight: bold;
        """)
    return button


def create_histogram_pixmap():
    path = '../../../../visualization/histogram.png'
    return QPixmap(path)


def create_histogram():
    histogram = QLabel('Histogram Image')
    histogram.setFixedHeight(500)
    return histogram


def create_histogram_title():
    hist_title = QLabel('Histogram')
    hist_title.setText('Histogram')
    hist_title.setStyleSheet("""
            color: black;
            margin: 0;
            padding: 0;
            font-weight: bold;
        """)
    return hist_title


def create_main_window():
    widget = QWidget()
    widget.setWindowTitle('Click Clock')
    widget.resize(1200, 900)
    widget.setStyleSheet("background-color:#e1e1e1;")
    return widget


def render():
    # Initialize application
    app = QApplication([])

    # Create histogram label
    histogram = QLabel('Histogram Image')
    histogram.setPixmap(create_histogram_pixmap())

    def refresh(event):
        histogram.setPixmap(create_histogram_pixmap())

    # Create refresh button
    button = create_refresh_button()
    button.clicked.connect(refresh)

    hist_title = create_histogram_title()

    # Create layout and add widgets
    layout = QVBoxLayout()
    layout.addWidget(button)
    # layout.addWidget(hist_title)
    layout.addWidget(histogram)

    # Apply layout to widget
    main_window = create_main_window()
    main_window.setLayout(layout)
    main_window.show()

    app.exec_()


if __name__ == '__main__':
    render()
