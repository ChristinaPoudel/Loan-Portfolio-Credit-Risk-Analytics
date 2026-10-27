
from pathlib import Path
import sqlite3
import pandas as pd

# Find the project folder.
project_folder = Path(__file__).resolve().parent.parent

# Set the file paths.
database_file = project_folder / "data" / "loan_portfolio.db"
sql_folder = project_folder / "sql"
output_file = project_folder / "reports" / "loan_portfolio_sql_reports.xlsx"

# List the SQL files to run.
sql_files = [
    "01_portfolio_overview.sql",
    "02_credit_score_risk.sql",
    "03_loan_purpose_risk.sql",
    "04_province_risk.sql",
    "05_portfolio_kpis.sql"
]

# Choose a worksheet name prefix for each SQL file.
sheet_names = {
    "01_portfolio_overview.sql": "Overview",
    "02_credit_score_risk.sql": "Credit_Score",
    "03_loan_purpose_risk.sql": "Loan_Purpose",
    "04_province_risk.sql": "Province",
    "05_portfolio_kpis.sql": "KPIs"
}

# Check that the database exists.
if not database_file.exists():
    raise FileNotFoundError(f"Database not found: {database_file}")

# Check that all SQL files exist.
for filename in sql_files:
    if not (sql_folder / filename).exists():
        raise FileNotFoundError(f"SQL file not found: {filename}")

# Create the reports folder if needed.
output_file.parent.mkdir(parents=True, exist_ok=True)

# Run the queries and save their results to Excel.
with sqlite3.connect(database_file) as connection:
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        for filename in sql_files:
            sql_file = sql_folder / filename
            sql_text = sql_file.read_text(encoding="utf-8")

            # Separate the SQL queries.
            queries = [
                query.strip()
                for query in sql_text.split(";")
                if query.strip()
            ]

            # Run each query and save its results.
            prefix = sheet_names[filename]

            for number, query in enumerate(queries, start=1):
                results = pd.read_sql_query(query, connection)
                worksheet = f"{prefix}_Q{number}"

                results.to_excel(
                    writer,
                    sheet_name=worksheet,
                    index=False
                )

                print(f"Exported: {worksheet} ({len(results)} rows)")

print("\nExcel export completed successfully!")
print(f"Saved to: {output_file}")
