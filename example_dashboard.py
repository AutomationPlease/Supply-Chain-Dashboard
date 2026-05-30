"""
Simple stripped down example snippet from my Supply Chain Dashboard build.
Demonstrates a way for pandas data loading and PySide6 table integration
"""

from PySide6.QtWidgets import (QApplication, QMainWindow, QTableView, 
                               QPushButton, QVBoxLayout, QWidget)
import pandas as pd
import sys
import os

class SupplyChainDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Supply Chain Dashboard - Example")
        self.resize(1000, 600)

        #Data Loading (not hardcoded)
        self.df = self.load_supply_chain_data()

        #Main widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        #Table View
        self.table = QTableView()
        self.table.setAlternatingRowColors(True)
        
        #Load data into table (full app would use a custom model)
        if not self.df.empty:
            self.table.setModel(self.create_table_model(self.df))

        #Export Button
        export_btn = QPushButton("Export to Excel")
        export_btn.clicked.connect(self.export_to_excel)

        layout.addWidget(self.table)
        layout.addWidget(export_btn)

        self.setCentralWidget(central_widget)

    def load_supply_chain_data(self):
        """Load data from file or simulate real loading"""
        try:
            #Try to load from a real data source
            if os.path.exists("data/materials_summary.xlsx"):
                return pd.read_excel("data/materials_summary.xlsx")
            elif os.path.exists("materials_summary.csv"):
                return pd.read_csv("materials_summary.csv")
        except Exception:
            pass
        
        #Fallback - empty or sample structure (never hardcoded business data)
        return pd.DataFrame(columns=['Material', 'Description', 'On_Hand', 'Location', 
                                   'Vendor', 'Last_Updated'])

    def create_table_model(self, df):
        #Simplified for example
        model = pd.DataFrame(df)  #placeholder
        return model  #in full app this would be proper Qt model 

    def export_to_excel(self):
        print("Exporting current view to Excel...")
        #In full app: self.df.to_excel("export.xlsx", index=False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SupplyChainDashboard()
    window.show()
    sys.exit(app.exec())
