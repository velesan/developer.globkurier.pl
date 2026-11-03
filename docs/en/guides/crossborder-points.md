---
title: Crossborder / Points
---

# Crossborder operation and points:
#### Wstęp
- Crossborder and PUDO point support is identical. 
- Crossborder is available as long as the product is included in the customer's price list.
- CollectionType in endpoint /products should contain an object with text CROSSBORDER or POINT:
            "`collectionTypes`": ["CROSSBORDER"]
- when selecting this product, we retrieve the shipping location via endpoint /points for `productId` = selected product along with other parameters - we will get a list of terminals / points. Alternatively, instead of `productId`, you can enter the carrier code and get a full list of points ([Get carrier datas (EN)](get-carrier-data.md))
- we insert the selected terminal (id) / point (id) as pointId in the senderAddress section.

#### Couriers for Crossborder:
* DHL DE
* Balikovna
* POST NORD DIRECT LINK
* Royal Mail
* Spring

#### For full integration:
* /products - products for the criteria
* /products/addons - add-ons for the selected product
* /points -> retrieve points for the crossborder/point product
* /order/price - total order calculation
* /order/validate - data validation
* /order - ordering


#### Fast path ([Fast order Integration (EN)](fast-order-integration.md)):
* the customer should be given the option to choose the category of additional services (a list can be created based on the endpoint) [Get available carrier list](../api/globkurier.md#/Carriers/carrierListR01))
* for valuation we use [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice) with parameter onlyPricing = true and we give collectionType as CROSSBORDER
* terminals / points can be downloaded via [Get shipment/receiving](../api/globkurier.md#/Points/pointGetList) for specific carriers
* After correct/confirmed quote, you can place an order in the same way - onlyPricing = false, createFully = true

#### Example

.../v1/order/bestPrice?onlyPricing=true&createFully=false

Body Type : application/json
{
    "shipment": {
        "length": 10,
        "width": 10,
        "height": 10,
        "weight": 5,
        "quantity": 1,
        "integrationName": "DHL DE"
    },
    "collectionType": "CROSSBORDER",
    "content": "gazety",
    "paymentId": 3,
    "receiverType": "PERSON",
    "receiverAddress": {
        "name": "rrr",
        "postCode": "32085",
        "city": "Berlin",
        "street": "august",
        "houseNumber": "2",
        "countryId": 23,
        "phone": "1234567890",
        "email": "odbiorca@example.com",
        "contactPerson": "testowy"
    },
    "senderAddress": {
        "name": "globkurier",
        "postCode": "41-160",
        "city": "Katowice",
        "street": "korfantego",
        "houseNumber": "128A",
        "countryId": 1,
        "phone": "321234567",
        "email": "biuro@globkurier.pl",
        "contactPerson": "testowy",
        "pointId":"ZGORZELEC"
    },
    "addons":{
        "INSURANCE": {"value":50}
    }    
}
