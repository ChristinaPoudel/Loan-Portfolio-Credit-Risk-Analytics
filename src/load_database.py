
from pathlib import Path
import sqlite3
import pandas as pd

# Find the project folder.
project_folder = Path(__file__).resolve().parent.parent

# Set the file paths.
csv_file = project_folder / "data" / "processed" / "loan_portfolio_cleaned.csv"
database_file = project_folder / "data" / "loan_portfolio.db"

# Check that the cleaned CSV exists.
if not csv_file.exists():
    raise FileNotFoundError(f"CSV file not found: {csv_file}")

# Read the cleaned data.
df = pd.read_csv(csv_file)

# Save the data to the SQLite database.
with sqlite3.connect(database_file) as connection:
    df.to_sql(
        "loan_portfolio",
        connection,
        if_exists="replace",
        index=False
    )

    # Check how many records were saved.
    result = connection.execute(
        "SELECT COUNT(*) FROM loan_portfolio"
    )
    record_count = result.fetchone()[0]

print("Database created successfully.")
print(f"Records loaded: {record_count:,}")
print(f"Database location: {database_file}")
