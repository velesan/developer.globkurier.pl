---
title: Order with customs
---

When ordering a shipment via the [Simplified order placement (bestprice)](../api/globkurier.md#/Orders/orderCreateBestPrice) or [Create order](../api/globkurier.md#/Orders/orderCreate) endpoint for exports of goods outside the EU, you can use electronic customs clearance. 

The customs section in the request is used for this. 
The fields and structure are dynamic and may differ for each carrier. Retrieve the information about required fields from [/customsRequiredFields](../api/globkurier.md#/Orders/orderGetCustomRequiredFields)
Retrieve the list of fields from [/customs/config](../api/globkurier.md#/Customs/customsGetDeclarationConfigR01) 

The endpoint requires the following parameters: 

- `productId` - Product identifier retrieved with the [/products](../api/globkurier.md#/Products/productSearch) resource
- `senderCountryId` and `receiverCountryId` - Sender/receiver country identifier retrieved with the [/countries](../api/globkurier.md#/Countries/countryListR01) resource
- `collectionType` - Collection type (PICKUP, POINT, CROSSBORDER)

Based on this, you can prepare the "customs" section. Example:


```
"customs": {
    "sender": {
        "eori": "PL1234567890"
    },
    "receiver": {
        "eori": "NL987654321"
    },
    "commodities": [
        {
            "description": "shirt ;; shirt",
            "composition": "100% cotton ;; 100% cotton",
            "purpose": "clothing ;; everyday use",
            "hsCode": "6105.10.0010",
            "countryOfOrigin": "PL",
            "unitOfMeasurement": "EA",
            "quantity": 2,
            "unitValue": 29.99,
            "unitWeightGross": 0.350,
            "unitWeightNet": 0.300,
            "subTotalValue": 59.98,
            "mid": null
        }
    ],
    "totalWeight": [
        {
            "unit": "EA",
            "weightGross": 0.700,
            "weightNet": 0.600
        }
    ],
    "currency": "EUR",
    "purpose": "SOLD",
    "invoiceNumber": "INV/2026/001",
    "invoiceDate": "2026-04-17",
    "postalCharges": 12.50,
    "vatRegistrationNumber": "PL1234563218",
    "vatRegistrationNumberReceiver": "NL123456789B01"
}
```
