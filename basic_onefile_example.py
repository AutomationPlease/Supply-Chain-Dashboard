from PySide6.QtWidgets import QStackedWidget, QPushButton, QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTableWidget, QComboBox
from PySide6.QtCore import Qt
import sys
import pandas as pd

#Data source load example
datasource_one = r"C:\\"

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Basic Application Build")
window.resize(900, 600)

#Central widget will hold the stacked pages (example)
central_widget = QWidget()
window.setCentralWidget(central_widget)

#Main layout (example)
main_layout = QVBoxLayout(central_widget)
main_layout.setContentsMargins(0, 0, 0, 0)

#Stacked widget for pages (example)
stack = QStackedWidget()
main_layout.addWidget(stack)

#Page 1 (example)
page1 = QWidget()
page1_layout = QVBoxLayout(page1)
page1_layout.setContentsMargins(20, 10, 20, 20)


title_label = QLabel("PYTHON BASIC DASHBOARD")
title_label.setAlignment(Qt.AlignCenter)
title_label.setStyleSheet("""
        QTableWidget {
            background-color: #1c1f26;
            color: #121217;
            gridline-color: #2a2a3f;
            alternate-background-color: #252538;
        }
        QHeaderView::section {
            background-color: #2a2a3f;
            color: white;
            padding: 8px;
            border: none;
            font-weight: bold;
        }
        QHeaderView::section:hover {
            background-color: #3a3a4f;
        }
        QTableWidget::item {
            padding: 6px;
        }
""")

page1_layout.addWidget(title_label)
page1_layout.addStretch(1)
stack.addWidget(page1)

#Page 2 (example)
page2 = QWidget()
page2_layout = QVBoxLayout(page2)
page2_layout.setContentsMargins(20, 20, 20, 20)
page2_layout.setSpacing(15)

#Page 2 title (example)
page2_title = QLabel("Page 2")
page2_title.setAlignment(Qt.AlignCenter)
page2_title.setStyleSheet("""
    font-size: 28px; 
    font-weight: bold; 
    color: #e5e5e5; 
    margin-bottom: 15px;
""")
page2_layout.addWidget(page2_title)

#load datasource (example)
try:
    df_datasource_one = pd.read_excel(datasource_one)

except Exception as e:
    print(f"Error loading IMM data: {e}")

#table (example)
material_combo = QComboBox()
material_combo.setStyleSheet("""
        QComboBox {
            background-color: #1a1a1a;
            color: #e5e5e5;
            border: 1px solid #2e2e2e;
            border-radius: 4px;
            padding: 8px;
            font-size: 16px;
        }
        QComboBox:hover {
            background-color: #222222;
        }
        QComboBox::drop-down {
            border: none;
        }
""")
                             
page2_layout.addWidget(material_combo)

material_table = QTableWidget()
material_table.setStyleSheet(""" 
        QTableWidget {
            background-color: #1a1a1a;
            color: #e5e5e5;
            gridline-color: #2e2e2e;
            alternate-background-color: #222222;
            border: none;
            selection-background-color: #3d3d3d;
        }

        QTableWidget::item {
            padding: 6px;
        }

        QTableWidget::item:hover {
            background-color: #2a2a2a;
            color: #ffffff;
        }

        QHeaderView::section {
            background-color: #2e2e2e;
            color: #e5e5e5;
            padding: 8px;
            border: none;
            font-weight: bold;
        }

        QHeaderView::section:hover {
            background-color: #3d3d3d;
        }

        QTableWidget::item:selected {
            background-color: #3d3d3d;
            color: #ffffff;
}
""")
material_table.horizontalHeader().setStretchLastSection(True)
material_table.verticalHeader().setVisible(False)
page2_layout.addWidget(material_table, stretch=1)

#Add page to stack (example)
stack.addWidget(page2)


#Navigation buttons (example)
nav_layout = QHBoxLayout()
nav_layout.setContentsMargins(20, 10, 20, 10)

btn_page1 = QPushButton("Page 1")
btn_page1.clicked.connect(lambda: stack.setCurrentIndex(0))
nav_layout.addWidget(btn_page1)

btn_page2 = QPushButton("Page 2")
btn_page2.clicked.connect(lambda: stack.setCurrentIndex(1))
nav_layout.addWidget(btn_page2)

main_layout.addLayout(nav_layout)

window.show()
sys.exit(app.exec())
