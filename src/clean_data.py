
from pathlib import Path
import pandas as pd

# Find the project folder.
project_folder = Path(__file__).resolve().parent.parent

# Set the input and output file paths.
input_file = project_folder / "data" / "raw" / "loan_portfolio_credit_risk_synthetic.csv"
output_file = project_folder / "data" / "processed" / "loan_portfolio_cleaned.csv"

# Check that the original CSV exists.
if not input_file.exists():
    raise FileNotFoundError(f"CSV file not found: {input_file}")

# Load the original data.
df = pd.read_csv(input_file)
original_count = len(df)

print("Starting data cleaning...")
print(f"Original records: {original_count:,}")

# Remove duplicate borrower IDs.
df = df.drop_duplicates(subset="borrower_id", keep="first")

# Remove rows missing important values.
required_columns = [
    "borrower_id",
    "loan_amount_cad",
    "annual_income_cad",
    "credit_score",
    "defaulted"
]
df = df.dropna(subset=required_columns)

# Keep rows with valid default values: 0 or 1.
df = df[df["defaulted"].isin([0, 1])]

# Keep positive loan amounts and incomes.
# Credit scores must be between 300 and 900.
df = df[
    (df["loan_amount_cad"] > 0)
    & (df["annual_income_cad"] > 0)
    & (df["credit_score"].between(300, 900))
]

# Create the output folder if it does not exist.
output_file.parent.mkdir(parents=True, exist_ok=True)

# Save the cleaned data.
df.to_csv(output_file, index=False)

# Show the results.
print(f"Cleaned records: {len(df):,}")
print(f"Records removed: {original_count - len(df):,}")
print(f"Defaulted loans: {int(df['defaulted'].sum()):,}")
print(f"Simulated default rate: {df['defaulted'].mean():.2%}")
print(f"\nCleaned data saved to:\n{output_file}")
