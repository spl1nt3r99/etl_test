-- Check for valid product names
select distinct product_name
from product_sales;

-- Check for non duplicates
select sale_id, count(*)
from product_sales
group by sale_id, product_id, sale_date, quantity, sales_price, product_price, product_name, category
having count(*) > 1