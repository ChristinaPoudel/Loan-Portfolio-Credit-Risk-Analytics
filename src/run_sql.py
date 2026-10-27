
from pathlib import Path
import sqlite3

# Find the project folder.
project_folder = Path(__file__).resolve().parent.parent

# Set the database and SQL folder paths.
database_file = project_folder / "data" / "loan_portfolio.db"
sql_folder = project_folder / "sql"

# List the SQL files in the order they should run.
sql_files = [
    sql_folder / "01_portfolio_overview.sql",
    sql_folder / "02_credit_score_risk.sql",
    sql_folder / "03_loan_purpose_risk.sql",
    sql_folder / "04_province_risk.sql",
    sql_folder / "05_portfolio_kpis.sql"
]

# Check that the database exists.
if not database_file.exists():
    raise FileNotFoundError(
        f"Database not found: {database_file}"
    )

# Check that all SQL files exist.
for sql_file in sql_files:
    if not sql_file.exists():
        raise FileNotFoundError(
            f"SQL file not found: {sql_file}"
        )

# Run the SQL queries.
with sqlite3.connect(database_file) as connection:
    for sql_file in sql_files:
        print("\n" + "=" * 50)
        print(f"FILE: {sql_file.name}")
        print("=" * 50)

        # Read the SQL file and separate its queries.
        sql_text = sql_file.read_text(encoding="utf-8")
        queries = [
            query.strip()
            for query in sql_text.split(";")
            if query.strip()
        ]

        # Run each query and display its results.
        for number, query in enumerate(queries, start=1):
            print(f"\n--- Query {number} ---")
            cursor = connection.execute(query)

            if cursor.description:
                column_names = [
                    column[0] for column in cursor.description
                ]
                print(" | ".join(column_names))

                for row in cursor.fetchall():
                    print(" | ".join(str(value) for value in row))

print("\nAll SQL files executed successfully.")
