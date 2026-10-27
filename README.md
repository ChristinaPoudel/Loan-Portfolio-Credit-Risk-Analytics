# Loan Portfolio & Credit Risk Analytics

## Project Overview

This project analyzes a **synthetic loan portfolio of 5,000 records** to explore credit risk, loan distribution, and simulated default patterns. It demonstrates an end-to-end data analytics workflow using Python, SQL, Excel, and Power BI.

The project was built for educational purposes to demonstrate data cleaning, validation, database querying, KPI development, and interactive dashboard reporting.

## Tools & Technologies

- **Python** — data validation, cleaning, and processing
- **Pandas** — data manipulation and analysis
- **SQLite** — relational database storage and querying
- **SQL** — portfolio KPIs and credit risk analysis
- **Excel** — exported SQL reports and analysis summaries
- **Power BI** — interactive dashboard and data visualization
- **Git & GitHub** — version control and project documentation

## Project Structure

```text
Loan-Portfolio-Credit-Risk-Analytics/
├── data/
│   ├── raw/
│   ├── processed/
│   └── loan_portfolio.db
├── sql/
│   ├── 01_portfolio_overview.sql
│   ├── 02_credit_score_risk.sql
│   ├── 03_loan_purpose_risk.sql
│   ├── 04_province_risk.sql
│   └── 05_portfolio_kpis.sql
├── src/
│   ├── validate_data.py
│   ├── clean_data.py
│   ├── load_database.py
│   ├── run_sql.py
│   └── export_reports.py
├── reports/
│   ├── loan_portfolio_sql_reports.xlsx
│   └── portfolio_insights.txt
├── dashboard/
│   └── Loan_Portfolio_Credit_Risk_Analytics.pbix
├── notebooks/
├── tests/
└── README.md
```

## Data Quality & Preparation

The synthetic dataset contains 5,000 loan records and 20 columns.

The data preparation workflow includes:

1. Validating the dataset structure and data types.
2. Checking for duplicate borrower IDs.
3. Checking missing values and key field constraints.
4. Validating loan amounts, annual incomes, credit scores, and default indicators.
5. Cleaning the dataset and exporting a processed CSV file.
6. Loading the cleaned data into a SQLite database.

Validation found no duplicate borrower IDs. Missing values in the simulated default date are intentional for records without a simulated default.

## Key Portfolio Metrics

| Metric | Result |
|---|---:|
| Total loan records | 5,000 |
| Simulated defaults | 268 |
| Simulated default rate | 5.36% |
| Total loan value | $98,147,350.90 CAD |
| Average loan amount | $19,629.47 CAD |
| Average credit score | 688.61 |
| Average annual income | $65,769.70 CAD |
| Average debt-to-income ratio | 33.18% |

## Key Findings

### Credit Score Risk

| Credit Score Group | Loans | Simulated Defaults | Simulated Default Rate |
|---|---:|---:|---:|
| Below 600 | 368 | 64 | 17.39% |
| 600–699 | 2,445 | 156 | 6.38% |
| 700–749 | 1,393 | 38 | 2.73% |
| 750 and above | 794 | 10 | 1.26% |

In this synthetic dataset, lower credit score groups have higher simulated default rates. The below-600 group has the highest rate, while the 750-and-above group has the lowest.

### Loan Purpose

Small business loans have the highest simulated default rate at 10.00%, followed by education loans at 7.61%.

These results describe this generated dataset only and should not be interpreted as actual lending industry patterns.

### Provincial Analysis

The analysis compares simulated default rates across ten Canadian provinces. New Brunswick has the highest observed simulated rate at 7.22%, while Newfoundland and Labrador has the lowest at 3.13%.

Province-level results should be interpreted cautiously because the number of records varies across provinces, and the dataset is synthetic.

## Power BI Dashboard

The interactive Power BI report includes:

- KPI cards for loan records, defaults, simulated default rate, loan value, average credit score, and average debt-to-income ratio.
- Simulated default rate by credit score group.
- Simulated default rate by loan purpose.
- Simulated default rate by province.
- A province slicer for interactive filtering.

**Report file:** `dashboard/Loan_Portfolio_Credit_Risk_Analytics.pbix`

## How to Run the Data Pipeline

Run these commands from the project root in PowerShell:

```powershell
python src/validate_data.py
python src/clean_data.py
python src/load_database.py
python src/run_sql.py
python src/export_reports.py
```

If using the project's virtual environment, activate it first:

```powershell
.\.venv\Scripts\Activate.ps1
```

The commands above assume the Python dependencies required by the scripts are installed in the active environment.

## Limitations

- All records are synthetic and do not represent actual Canadian borrowers or lending outcomes.
- The simulated default rate is not an estimate of the real-world Canadian loan default rate.
- The project demonstrates descriptive analytics, not a validated credit approval or default prediction model.
- Observed patterns are specific to the generated dataset.

## Data Disclaimer

**All loan records, default indicators, and default rates in this project are synthetic and intended for educational and portfolio demonstration purposes only. They do not represent actual Canadian borrowers, lenders, or lending outcomes.**
