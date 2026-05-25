# Supply Chain Dashboard

A full-featured **PySide6 / PyQt6** desktop application developed to provide real-time visibility and analytics for supply chain operations.

![Main Application Window](screenshots/main-window.png)

## Overview

This internal tool was built to consolidate multiple data sources into a single, user-friendly desktop interface for procurement, inventory, and demand planning teams.

## Key Features

- Multi-tab analytical interface (Summary, Detailed Views, Aged Analysis, Materials, Demand, etc.)
- Interactive Customer Location Map with detailed information pop-ups
- Configurable data source management
- Excel export functionality from all table views
- Real-time data refresh capabilities
- Visual demand charts with multi-filter selections
  - Select multiple items, multiple locations, specific time frames

## Screenshots


[**NOTE: Data shown is being simulated/faked to protect the data integrity of the company**]
![IMM Summary](screenshots/imm-summary.png)

![Customer Map](screenshots/customer-map.png)

[**NOTE: Data source file paths and names are being blocked out to protect the data integrity of the company**]
![Settings Panel](screenshots/settings.png)

![Demand Page - One Item, One Location (24 weeks)](screenshots/demand-page%2C%20one%20item%2C%20one%20location%2C%20show%2024%20weeks.png)

![Demand Page - One Item, Two Locations (8 weeks)](screenshots/demand-page%2C%20one%20item%2C%20two%20locations%2C%20show%208%20weeks.png)

![Demand Page - Two Items, One Location (6 weeks)](screenshots/demand-page%2C%20two%20items%2C%20one%20location%2C%20show%206%20weeks.png)

Additional customer map for if Folium is out of company library install policy. This map includes a simple straight line customer distance calculator, and is made using Plotly.
[**NOTE: Key ID label names are being blocked out to protect the data integrity of the company**]
![Customer Map 2](screenshots/customer-map-2.png)

## Technologies Used

- **Frontend**: PySide6 / PyQt6 (Python GUI framework)
- **Data Processing**: pandas, numpy, openpyxl
- **Visualization**: Custom Qt tables + Leaflet map integration
- **Architecture**: Model-View architecture with background threading for responsive UI

## Business Impact

- Significantly improved supply chain visibility across hundreds of materials
- Reduced manual work by consolidating disparate Excel-based processes
- Enabled faster, data-driven decision making for planning and procurement teams

## Note

This repository is for demonstration purposes only. Due to the proprietary nature of the original internal tool:
- Source code is not included
- Some business-specific logic and data have been redacted
- Screenshots show representative functionality

## Skills Demonstrated

- Full lifecycle desktop application development
- Complex data integration and ETL processes
- Building intuitive user interfaces for technical and non-technical users
- Supply chain systems thinking and domain knowledge

---

**Made using Python**
