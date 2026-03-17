create database amazon_analysis;
use amazon_analysis;
select category, sum(TotalAmount) as Revenue 
from amazon 
group by category 
order by Revenue desc;

select category, count(*) as total_orders
from amazon
group by category 
order by total_orders desc;

select category, AVG(TotalAmount) as Avg_Order_Value
from amazon 
group by category 
order by Avg_Order_Value desc;

select country, SUM(TotalAmount) as CRevenue
from amazon 
group by country 
order by CRevenue desc;

select brand, sum(TotalAmount) as revenue 
from amazon 
group by brand 
order by revenue desc 
limit 10;

select year(OrderDate) as year, SUM(TotalAmount) as revenue 
from amazon 
group by year 
order by revenue desc;

select CustomerID, SUM(TotalAmount) as total_spent
from amazon 
group by CustomerID
order by total_spent desc
limit 10;

select SUM(TotalAmount) as total_revenue
from amazon;

select sum(total_spent)
from (
select CustomerID,
SUM(TotalAmount) as total_spent
from amazon 
group by CustomerID 
order by total_spent desc 
limit 100
) as TopCustomers;






