---
title: Pricing Summary before ordering
---

## Order summary
Before placing your order, you can download the full order settlement along with discount code verification. 

For this we use endpoint [Get order price](../api/globkurier.md#/Order%20Pricing/orderGetPrice). 
The endpoint accepts similar parameters as the endpoint for placing an order [Create order](../api/globkurier.md#/Orders/orderCreate). Please provide all the data provided by the client.
Instead of providing the shipment parameters in the body section, we send them in the URL as parameters.
In return, we will receive detailed information related to the settlement of the order:

| Field | Description |
|-------|-------------|
| `currency` | CURRENCY |
| `taxType` | VAT type |
| `vatPercent` | VAT rate |
| `totalGrossPrice` | total gross amount |
| `totalNetPrice` | total net amount |
| `netPriceWithoutFuelSurcharge` | net amount without fuel surcharge |
| `productNetPrice` | net product amount |
| `productsNetPrice` | sum of net amounts for the product with discount |
| `productsGrossPrice` | sum of gross amounts for the product with discount |
| `productsStockNetPrice` | sum of net amounts for the product without discount |
| `productsStockGrossPrice` | sum of gross amounts for the product without discount |
| `fuelSurchargeNetPrice` | fuel surcharge with discount - net |
| `fuelSurchargeGrossPrice` | fuel surcharge with discount - gross |
| `fuelSurcharge` | fee Fuel - deprecated field |
| `fuelSurchargeStockNetPrice` | fuel surcharge without discount - net |
| `fuelSurchargeStockGrossPrice` | fuel surcharge without discount - gross |
| `addonsNetPrice` | net amount for add-ons |
| `addonsGrossPrice` | gross amount for add-ons |
| `discountNetPrice` | discount amount applied |
| `packages[]` | List of shipment components. |
| `addons[]` | List of add-ons that present net (price) and gross (priceGross) amounts after calculating the discount |
