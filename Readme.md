<h3 style='font-size:3em; line-height:0px;'> Rock Scalers </h3>
<h3 style='font-size:1.37em; line-height:0.5em'> For all your climbing needs </h3>
<p style='line-height:0px;'>An SQLite Database assignment<br></p>
<p style='line-height:0px;'>By Lincoln MURRAY (Student)</p>

# Part 1
## Outline

## Timeline
<img src='images/Timeline.jpg'>  

## Description
### Requirements
### Ethical, Legal and Security issues
### Quality of Data

## Design
### Entity Relationship Diagram
<img src='images/Entity Relationship Diagram.jpg'>  

### Relational Notation
<pre>
Products(<u>ProductID</u>, ManufacturerID (FK), Description)

Manufacturers(<u>ManufacturerID</u>, Location, DateFounded)

Product-Supplier(<u>ProductID</u> (FK), <u>SupplierID</u> (FK), ProductURL, Price)

Suppliers(<u>SupplierID</u>, SupplierURL)

Product-Order(<u>ProductID</u> (FK), <u>OrderID</u> (FK))

Orders(<u>OrderID</u>, <u>CustomerID</u> (FK), DeliveryAddress, BillingAddress, DeliveryRequest, Total)

Customers(<u>CustomerID</u>, Name)

</pre>

### Data Dictionary
<table><thead>
  <tr>
    <th>Element Name</th>
    <th>Data Type</th>
    <th>Description</th>
    <th>Constraints</th>
  </tr></thead>
<tbody>
  <tr>
    <td>ProductID</td>
    <td>Integer</td>
    <td>A Unique identify for each product.</td>
    <td>Must be unique, &gt;= 0 and not null</td>
  </tr>
  <tr>
    <td>ManufacturerID</td>
    <td>Integer</td>
    <td>A Unique identify for each manufacturer.</td>
    <td>Must be unique, &gt;= 0 and not null</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>String</td>
    <td>The descriptor for each product.</td>
    <td>No constraints</td>
  </tr>
  <tr>
    <td>Location</td>
    <td>String</td>
    <td>General location of the manufactuer companies origin.</td>
    <td>Max Length 50 Characters</td>
  </tr>
  <tr>
    <td>DateFounded</td>
    <td>Integer</td>
    <td>Year the company was founded</td>
    <td>Must be &gt; 0, &lt;= Current Year and not null</td>
  </tr>
  <tr>
    <td>SupplierID</td>
    <td>Integer</td>
    <td>A Unique identify for each supplier.</td>
    <td>Must be unique, &gt;= 0 and not null</td>
  </tr>
  <tr>
    <td>ProductURL</td>
    <td>String</td>
    <td>The URL to order the product.</td>
    <td>Max Length 100 Characters and not null</td>
  </tr>
  <tr>
    <td>Price</td>
    <td>Float</td>
    <td>The price of the product</td>
    <td>Must be &gt; 0 and not null</td>
  </tr>
  <tr>
    <td>SupplierURL</td>
    <td>String</td>
    <td>The URL to view the suppliers website</td>
    <td>Max Length 100 Characters and not null</td>
  </tr>
  <tr>
    <td>OrderID</td>
    <td>Integer</td>
    <td>A Unique identify for each order.</td>
    <td>Must be unique, &gt;= 0 and not null</td>
  </tr>
  <tr>
    <td>CustomerID</td>
    <td>Integer</td>
    <td>A Unique identify for each customer.</td>
    <td>Must be unique, &gt;= 0 and not null</td>
  </tr>
  <tr>
    <td>DeliveryAddress</td>
    <td>String</td>
    <td>The Address for the order to be delivered to.</td>
    <td>Max Length 200 Characters and not null</td>
  </tr>
  <tr>
    <td>BillingAddress</td>
    <td>String</td>
    <td>The Billing address required by law to invoice the purchase to.</td>
    <td>Max Length 200 Characters</td>
  </tr>
  <tr>
    <td>DeliveryRequest</td>
    <td>String</td>
    <td>Any special requests for the delivery such as ATL.</td>
    <td>Max length 500 Characters</td>
  </tr>
  <tr>
    <td>Total</td>
    <td>Float</td>
    <td>The price of the order.</td>
    <td>Must be &gt;= 0 and not null</td>
  </tr>
  <tr>
    <td>Name</td>
    <td>String</td>
    <td>The Customer name used for shipping and addressing them.</td>
    <td>Max Length 50 Characters</td>
  </tr>
</tbody></table>

### Outline of Queries
# Part 2