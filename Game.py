import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QListWidget, QListWidgetItem, QLineEdit, QMessageBox, QInputDialog
)
from PyQt6.QtGui import QIcon, QPixmap, QPainter, QFont
from PyQt6.QtCore import Qt


def get_fruit_icon(fruit):
    """
    Try to load the icon for a fruit from the 'icons' folder.
    If not found, create a dummy icon with the fruit name.
    """
    icon_path = os.path.join("icons", f"{fruit.lower()}.png")
    pixmap = QPixmap(icon_path)
    if pixmap.isNull():
        # Create a dummy icon if the image file is missing.
        pixmap = QPixmap(64, 64)
        pixmap.fill(Qt.GlobalColor.lightGray)
        painter = QPainter(pixmap)
        painter.setPen(Qt.GlobalColor.black)
        font = QFont("Arial", 10)
        painter.setFont(font)
        painter.drawText(pixmap.rect(), Qt.AlignmentFlag.AlignCenter, fruit)
        painter.end()
    return QIcon(pixmap)


class OwnerWindow(QWidget):
    def __init__(self, store):
        super().__init__()
        self.setWindowTitle("Owner Mode - Manage Store")
        self.store = store

        # Set a store background image if available, otherwise use a default color.
        if os.path.exists("store_background.jpg"):
            self.setStyleSheet("background-image: url('store_background.jpg');")
        else:
            self.setStyleSheet("background-color: lightblue;")

        self.layout = QVBoxLayout()

        # Label and list of current fruits.
        self.label = QLabel("Current Fruits in Store:")
        self.layout.addWidget(self.label)

        self.listWidget = QListWidget()
        self.updateList()
        self.layout.addWidget(self.listWidget)

        # Layout for adding new fruit.
        self.inputLayout = QHBoxLayout()
        self.fruitNameInput = QLineEdit()
        self.fruitNameInput.setPlaceholderText("Fruit Name")
        self.inputLayout.addWidget(self.fruitNameInput)

        self.priceInput = QLineEdit()
        self.priceInput.setPlaceholderText("Price")
        self.inputLayout.addWidget(self.priceInput)

        self.layout.addLayout(self.inputLayout)

        # Button to add a new fruit.
        self.addButton = QPushButton("Add Fruit")
        self.addButton.clicked.connect(self.addFruit)
        self.layout.addWidget(self.addButton)

        self.setLayout(self.layout)

    def updateList(self):
        """Refresh the list widget with current fruits and their prices."""
        self.listWidget.clear()
        for fruit, price in self.store.items():
            item = QListWidgetItem(f"{fruit}: ${price:.2f}")
            item.setIcon(get_fruit_icon(fruit))
            self.listWidget.addItem(item)

    def addFruit(self):
        fruit = self.fruitNameInput.text().strip()
        try:
            price = float(self.priceInput.text().strip())
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Price must be a number.")
            return

        if fruit in self.store:
            QMessageBox.information(self, "Duplicate", f"{fruit} already exists in the store.")
        else:
            self.store[fruit] = price
            self.updateList()
            QMessageBox.information(self, "Success", f"{fruit} added to the store.")
            self.fruitNameInput.clear()
            self.priceInput.clear()


class CustomerWindow(QWidget):
    def __init__(self, store):
        super().__init__()
        self.setWindowTitle("Customer Mode - Buy Fruit")
        self.store = store

        # Set a store background image if available, otherwise use a default color.
        if os.path.exists("store_background.jpg"):
            self.setStyleSheet("background-image: url('store_background.jpg');")
        else:
            self.setStyleSheet("background-color: lightblue;")

        self.layout = QVBoxLayout()
        self.label = QLabel("Available Fruits:")
        self.layout.addWidget(self.label)

        self.fruitListWidget = QListWidget()
        self.updateList()
        # Double-clicking a fruit starts the purchase process.
        self.fruitListWidget.itemDoubleClicked.connect(self.purchaseFruit)
        self.layout.addWidget(self.fruitListWidget)

        self.setLayout(self.layout)

    def updateList(self):
        """Refresh the fruit list with current store inventory."""
        self.fruitListWidget.clear()
        for fruit, price in self.store.items():
            item = QListWidgetItem(f"{fruit}: ${price:.2f}")
            item.setIcon(get_fruit_icon(fruit))
            self.fruitListWidget.addItem(item)

    def purchaseFruit(self, item):
        fruit_info = item.text().split(":")
        fruit = fruit_info[0]
        price = self.store.get(fruit, 0)
        # Ask if the customer has a membership (applies discount if yes).
        membership, ok = QInputDialog.getItem(
            self, "Membership", "Do you have a membership?",
            ["Yes", "No"], 0, False
        )
        if ok:
            final_price = price * 0.9 if membership == "Yes" else price
            QMessageBox.information(self, "Purchase", f"You purchased {fruit} for ${final_price:.2f}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fruit Store Game")
        self.setGeometry(100, 100, 300, 200)

        # The store dictionary holds fruit names and prices.
        self.store = {
            "Apple": 1.00,
            "Banana": 1.20,
            "Orange": 1.50,
        }

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout()

        self.label = QLabel("Are you an Owner or a Customer?")
        layout.addWidget(self.label)

        self.ownerButton = QPushButton("Owner")
        self.ownerButton.clicked.connect(self.openOwnerMode)
        layout.addWidget(self.ownerButton)

        self.customerButton = QPushButton("Customer")
        self.customerButton.clicked.connect(self.openCustomerMode)
        layout.addWidget(self.customerButton)

        centralWidget.setLayout(layout)

    def openOwnerMode(self):
        self.ownerWindow = OwnerWindow(self.store)
        self.ownerWindow.show()

    def openCustomerMode(self):
        self.customerWindow = CustomerWindow(self.store)
        self.customerWindow.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())