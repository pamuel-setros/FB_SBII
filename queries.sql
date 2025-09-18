
-- Daily items sold and running total
SELECT 
	DATE(InvoiceDate) AS InvoiceDate, 
	SUM(Quantity) AS items_sold,
	SUM(SUM(Quantity)) OVER (ORDER BY DATE(InvoiceDate)) AS running_total
FROM online_retail
GROUP BY DATE(InvoiceDate)
ORDER BY DATE(InvoiceDate);

-- Daily revenue (money coming in) with running total and country
SELECT 
	DATE(InvoiceDate) AS InvoiceDate,
	Country,
	SUM(Quantity * UnitPrice) AS daily_revenue,
	SUM(SUM(Quantity * UnitPrice)) OVER (PARTITION BY Country ORDER BY DATE(InvoiceDate)) AS running_total
FROM online_retail
GROUP BY Country, DATE(InvoiceDate)
ORDER BY Country, DATE(InvoiceDate);