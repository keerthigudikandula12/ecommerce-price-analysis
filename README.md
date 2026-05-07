# E-Commerce Price Drop & Demand Tracker

## Overview
Analysed 1,400+ Amazon product listings to uncover pricing patterns,
discount trends, and value opportunities across categories.

Built using Python, SQL (SQLite), and Excel — covering the full
analyst workflow from raw data to stakeholder report.

---

## Business Questions Answered
- Which product categories have the highest average discounts?
- How are prices distributed across different price ranges?
- Does a higher discount mean lower product quality?
- Which products are genuine deals vs "value traps"?
- Which products offer the best absolute savings in rupees?

---

## Tech Stack

| Tool          | Used for                                       |
|---------------|------------------------------------------------|
| Python/Pandas | Data cleaning, EDA, calculations              |
| SQL (SQLite)  | 5 analytical queries (GROUP BY, CASE WHEN...)  |
| Matplotlib    | 5 data visualisation charts                    |
| Seaborn       | Chart styling                                  |
| openpyxl      | Automated 6-sheet Excel dashboard              |

---

## Project Structure

```
price_tracker/
├── 01_clean.py            # Load and clean raw CSV data
├── 02_sql_analysis.py     # 5 SQL queries on SQLite database
├── 03_visualise.py        # 5 charts (bar, boxplot, scatter...)
├── 04_excel_report.py     # Automated Excel dashboard (6 sheets)
├── README.md              # Project documentation
├── .gitignore             # Files excluded from GitHub
└── outputs/
    ├── clean_data.csv     # Cleaned dataset
    ├── dashboard.xlsx     # Final Excel report
    └── charts/            # 5 PNG chart images
```

---

## How to Run

**1. Download the dataset**
Download the Amazon Sales Dataset from Kaggle:
https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset

Save the file as `amazon.csv` inside the `price_tracker` folder.

**2. Install dependencies**
```
pip install pandas numpy matplotlib seaborn openpyxl
```

**3. Run files in order**
```
python 01_clean.py
python 02_sql_analysis.py
python 03_visualise.py
python 04_excel_report.py
```

---

## Key Findings

- **Electronics** has the highest average discount at **48%+**
- Over **60% of products** are priced under ₹1,000 after discount
- Products with **50%+ discount** have slightly lower avg ratings (3.8 vs 4.1)
  — but discounts are largely genuine, not quality red flags
- Identified top 10 **"best value"** products: 40%+ discount + 4.0+ rating
- Identified top 10 **"value traps"**: high discount but rating below 3.5

---

## Charts Generated

| Chart | Question Answered |
|-------|------------------|
| Avg discount by category | Which categories discount the most? |
| Price spread boxplot | How varied are prices per category? |
| Rating vs discount scatter | Do discounts signal poor quality? |
| Price bucket bar chart | Where are most products priced? |
| Top savings bar chart | Which products save the most money? |

---

## Dataset
**Amazon Sales Dataset** — Kaggle  
Source: https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset

---

## Author
Data Analyst | Python · SQL · Excel  
Hyderabad, India
