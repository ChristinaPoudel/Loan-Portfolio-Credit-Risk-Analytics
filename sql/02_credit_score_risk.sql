
-- Compare simulated default rates by credit score.

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
