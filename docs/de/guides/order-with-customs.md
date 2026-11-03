---
title: Order with customs
---

Bei der Bestellung einer Sendung über den Endpunkt [Simplified order placement (bestprice)](../api/globkurier.md#/Orders/orderCreateBestPrice) oder [Create order](../api/globkurier.md#/Orders/orderCreate) kann für die Ausfuhr von Waren außerhalb der EU die elektronische Zollabfertigung genutzt werden. 

Dafür dient der Abschnitt customs in der Anfrage (request). 
Die Felder und die Struktur sind dynamisch und können für jeden Carrier unterschiedlich sein. Die Informationen zu den erforderlichen Feldern sind über [/customsRequiredFields](../api/globkurier.md#/Orders/orderGetCustomRequiredFields) abzurufen
Die Liste der Felder ist über [/customs/config](../api/globkurier.md#/Customs/customsGetDeclarationConfigR01) abzurufen 

Der Endpunkt erfordert die folgenden Parameter: 

- `productId` - Produktkennung, abgerufen mit der Ressource [/products](../api/globkurier.md#/Products/productSearch)
- `senderCountryId` und `receiverCountryId` - Kennung des Absender-/Empfängerlandes, abgerufen mit der Ressource [/countries](../api/globkurier.md#/Countries/countryListR01)
- `collectionType` - Versandart (PICKUP, POINT, CROSSBORDER)

Auf dieser Grundlage kann der Abschnitt "customs" vorbereitet werden. Beispiel:


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
