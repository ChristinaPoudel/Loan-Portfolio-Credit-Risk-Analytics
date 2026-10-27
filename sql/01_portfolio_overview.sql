
-- 1. Count all loans.
SELECT COUNT(*) AS total_loans
FROM loan_portfolio;

-- 2. Count loans by default status.
SELECT
    defaulted,
    COUNT(*) AS loan_count
FROM loan_portfolio
GROUP BY defaulted
ORDER BY defaulted;

-- 3. Find the average loan amount.
SELECT ROUND(AVG(loan_amount_cad), 2) AS average_loan_amount_cad
FROM loan_portfolio;

-- 4. Find the total value of all loans.
SELECT ROUND(SUM(loan_amount_cad), 2) AS total_loan_amount_cad
FROM loan_portfolio;

-- 5. Find the average credit score.
SELECT ROUND(AVG(credit_score), 2) AS average_credit_score
FROM loan_portfolio;

-- 6. Compare simulated default rates by credit score group.
SELECT
    CASE
        WHEN credit_score < 600 THEN 'Below 600'
        WHEN credit_score < 700 THEN '600-699'
        WHEN credit_score < 750 THEN '700-749'
        ELSE '750 and above'
    END AS credit_score_group,
    COUNT(*) AS total_loans,
    SUM(defaulted) AS defaulted_loans,
    ROUND(AVG(defaulted) * 100, 2) AS simulated_default_rate_pct
FROM loan_portfolio
GROUP BY credit_score_group
ORDER BY
    CASE credit_score_group
        WHEN 'Below 600' THEN 1
        WHEN '600-699' THEN 2
        WHEN '700-749' THEN 3
        ELSE 4
    END;
