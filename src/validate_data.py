
from pathlib import Path
import pandas as pd

# Find the project folder and data file.
project_folder = Path(__file__).resolve().parent.parent
csv_file = project_folder / "data" / "raw" / "loan_portfolio_credit_risk_synthetic.csv"

# Check that the file exists.
if not csv_file.exists():
    raise FileNotFoundError(f"CSV file not found: {csv_file}")

# Read the CSV file.
df = pd.read_csv(csv_file)

print("=" * 40)
print("LOAN PORTFOLIO DATA CHECK")
print("=" * 40)

# Show the number of rows and columns.
print(f"\nNumber of records: {len(df):,}")
print(f"Number of columns: {len(df.columns)}")

# Check for duplicate borrower IDs.
duplicates = df["borrower_id"].duplicated().sum()
print(f"\nDuplicate borrower IDs: {duplicates}")

# Show columns that contain missing values.
print("\nMissing values:")
missing_values = df.isna().sum()
missing_values = missing_values[missing_values > 0]

if missing_values.empty:
    print("No missing values found.")
else:
    print(missing_values.to_string())

# Count defaulted and non-defaulted loans.
print("\nDefault counts:")
print(df["defaulted"].value_counts().sort_index())

# Calculate the simulated default rate.
default_rate = df["defaulted"].mean() * 100
print(f"\nSimulated default rate: {default_rate:.2f}%")

# Check that the data follows basic rules.
print("\nData checks:")
print("Borrower IDs are unique:", df["borrower_id"].is_unique)
print("Default values are 0 or 1:", set(df["defaulted"].unique()).issubset({0, 1}))
print("Loan amounts are positive:", (df["loan_amount_cad"] > 0).all())
print("Annual incomes are positive:", (df["annual_income_cad"] > 0).all())
print("Credit scores are between 300 and 900:", df["credit_score"].between(300, 900).all())

print("\nData check complete.")
