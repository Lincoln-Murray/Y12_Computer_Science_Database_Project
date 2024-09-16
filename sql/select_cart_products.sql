select products.Product_ID, products.Product_Name as 'Product', productssupplier.Image_URL as 'Image', productssupplier.Price
from orders
join productsorders on orders.OrderID = productsorders.Order_ID
join products on productsorders.Product_ID = products.Product_ID
join productssupplier on products.Product_ID = productssupplier.Product_ID
where orders.OrderID = 2
group by concat(orders.OrderID, products.Product_ID);