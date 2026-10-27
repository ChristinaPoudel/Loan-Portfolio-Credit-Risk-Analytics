
-- Calculate the main loan portfolio KPIs.
-- All data is synthetic and for educational purposes.

SELECT
    COUNT(*) AS total_loans,
    SUM(defaulted) AS total_defaults,
    ROUND(AVG(defaulted) * 100, 2) AS simulated_default_rate_pct,
    ROUND(SUM(loan_amount_cad), 2) AS total_loan_value_cad,
    ROUND(AVG(loan_amount_cad), 2) AS average_loan_amount_cad,
    ROUND(AVG(credit_score), 2) AS average_credit_score,
    ROUND(AVG(annual_income_cad), 2) AS average_annual_income_cad,
    ROUND(AVG(debt_to_income_ratio) * 100, 2) AS average_dti_pct
FROM loan_portfolio;
