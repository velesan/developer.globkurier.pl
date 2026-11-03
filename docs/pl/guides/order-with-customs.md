---
title: Order with customs
---

Przy zamawianiu przesyłki poprzez endpoint [Simplified order placement (bestprice)](../api/globkurier.md#/Orders/orderCreateBestPrice) lub [Create order](../api/globkurier.md#/Orders/orderCreate) dla wywozu towarów poza UE można skorzystać z elektronicznej odprawy celnej. 

Służy do tego sekcja customs w request. 
Pola i struktura są dynamiczne i dla każdego przewoźnika mogą być inne. Informację o wymaganych polach należy pobrać [/customsRequiredFields](../api/globkurier.md#/Orders/orderGetCustomRequiredFields)
Listę pól należy pobrać  [/customs/config](../api/globkurier.md#/Customs/customsGetDeclarationConfigR01) 

Endpoint wymaga podania parametrów: 

- `productId` - Identyfikator produktu pobrany za pomocą zasobu [/products](../api/globkurier.md#/Products/productSearch)
- `senderCountryId`  oraz `receiverCountryId` - Identyfikator kraju nadawcy/odbiorcy pobrany za pomocą zasobu [/countries](../api/globkurier.md#/Countries/countryListR01)
- `collectionType` - Typ nadania (PICKUP, POINT, CROSSBORDER)

Na tej podstawie można przygotować sekcję "customs". Przykład:


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
