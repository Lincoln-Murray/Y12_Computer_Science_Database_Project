SELECT 'Products'.'product id', 'Products'.'product name', 'Products'.'Description', 'Products-Supplier'.price, 'manufacturer'.' name' 
FROM Products
join 'Products-Supplier' on 'Products'.'Product ID' = 'Products-Supplier'.'Product ID'
join 'Manufacturer' on 'Products'.'Manufacturer ID' = 'Manufacturer'.'Manufacturer ID'