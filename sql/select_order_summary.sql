select orders.OrderID, customers.Name, orders.Date, SUM(productssupplier.Price)/2 as Total
from orders
join customers on orders.CustomerID = customers.CustomerID
join productsorders on orders.OrderID = productsorders.Order_ID
join products on productsorders.Product_ID = products.Product_ID
join productssupplier on products.Product_ID = productssupplier.Product_ID
WHERE orders.OrderID = -2
GROUP by orders.OrderID || customers.CustomerID
order by customers.name;