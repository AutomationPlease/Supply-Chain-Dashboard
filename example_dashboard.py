"""
Basic Very Stripped Down Example snippet from Supply Chain Dashboard
Demonstrates pandas data loading and PySide6 table integration
"""

from PySide6.QtWidgets import (QApplication, QMainWindow, QTableView, QPushButton, QVBoxLayout, QWidget)
import pandas as pd
import sys
import os

class SupplyChainDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Supply Chain Dashboard - Example")
        self.resize(1000, 600)

        #data Loading
        self.df = self.load_supply_chain_data()

        #main widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        #table View
        self.table = QTableView()
        self.table.setAlternatingRowColors(True)
        
        #load data into table (in real app you'd use a custom model)
        if not self.df.empty:
            self.table.setModel(self.create_table_model(self.df))

        #export button
        export_btn = QPushButton("Export to Excel")
        export_btn.clicked.connect(self.export_to_excel)

        layout.addWidget(self.table)
        layout.addWidget(export_btn)

        self.setCentralWidget(central_widget)

    def load_supply_chain_data(self):
        try:
            #try to load from example data source
            if os.path.exists("data/materials_summary.xlsx"):
                return pd.read_excel("data/materials_summary.xlsx")
            elif os.path.exists("materials_summary.csv"):
                return pd.read_csv("materials_summary.csv")
        except Exception:
            pass
        
        #example fallback - sample structure
        return pd.DataFrame(columns=['Material', 'Description', 'Stock', 'Location', 
                                   'Vendor', 'Last_Updated'])

    def create_table_model(self, df):
        """In real app this would be your custom BasePandasTableModel"""
        #simplified for example
        model = pd.DataFrame(df)  #placeholder
        return model

    def export_to_excel(self):
        print("Exporting current view to Excel...")
        #in real app it would be more something like: self.df.to_excel("export.xlsx", index=False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SupplyChainDashboard()
    window.show()
    sys.exit(app.exec())
