
-- Simulated credit risk by province
-- Uses synthetic educational data.

SELECT
    province,
    COUNT(*) AS total_loans,
    SUM(defaulted) AS defaulted_loans,
    ROUND(AVG(defaulted) * 100, 2) AS simulated_default_rate_pct,
    ROUND(AVG(loan_amount_cad), 2) AS average_loan_amount_cad
FROM loan_portfolio
GROUP BY province
ORDER BY simulated_default_rate_pct DESC;

