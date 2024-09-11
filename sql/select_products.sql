SELECT 'products'.'product_id', 'products'.'product_name', 'products'.'Description', 'productssupplier'.price, 'manufacturer'.'name', 'productssupplier'.Image_URL
FROM products
join 'productssupplier' on 'products'.'Product_ID' = 'productssupplier'.'Product_ID'
join 'manufacturer' on 'products'.'Manufacturer_ID' = 'manufacturer'.'Manufacturer_ID';