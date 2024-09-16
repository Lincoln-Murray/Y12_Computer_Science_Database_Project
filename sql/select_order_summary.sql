select orders.OrderID, customers.Name, orders.Date, SUM(productssupplier.Price) as Total
from orders
join customers on orders.CustomerID = customers.CustomerID
join productsorders on orders.OrderID = productsorders.Order_ID
join products on productsorders.Product_ID = products.Product_ID
join productssupplier on products.Product_ID = productssupplier.Product_ID
GROUP by customers.CustomerID, orders.OrderID
order by customers.name;