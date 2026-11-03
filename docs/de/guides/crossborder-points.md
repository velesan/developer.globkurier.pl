---
title: Crossborder / Points
---

## Crossborder-Betrieb und Punkte:
### Einleitung
- Die Unterstützung von Crossborder und PUDO-Punkten ist identisch. 
- Crossborder ist verfügbar, solange das Produkt in der Preisliste des Kunden enthalten ist.
- CollectionType im Endpunkt /products sollte ein Objekt mit dem Text CROSSBORDER oder POINT enthalten:
            "`collectionTypes`": ["CROSSBORDER"]
- Bei Auswahl dieses Produkts rufen wir den Versandort über den Endpunkt /points für `productId` = ausgewähltes Produkt zusammen mit den übrigen Parametern ab - wir erhalten eine Liste von Terminals / Punkten. Alternativ kann statt `productId` der Carrier-Code angegeben werden, um eine vollständige Liste der Punkte zu erhalten ([Get carrier datas (DE)](get-carrier-data.md))
- Das ausgewählte Terminal (id) / den ausgewählten Punkt (id) tragen wir als pointId im Abschnitt senderAddress ein.

### Kurierdienste für Crossborder:
* DHL DE
* Balikovna
* POST NORD DIRECT LINK
* Royal Mail
* Spring

### Für die vollständige Integration:
* /products - Produkte für die Kriterien
* /products/addons - Zusatzservices für das ausgewählte Produkt
* /points -> Punkte für das Crossborder-/Punkt-Produkt abrufen
* /order/price - Gesamtberechnung der Bestellung
* /order/validate - Datenvalidierung
* /order - Bestellung aufgeben


### Schneller Pfad ([Fast order Integration (DE)](fast-order-integration.md)):
* dem Kunden sollte die Möglichkeit gegeben werden, die Kategorie der Zusatzservices auszuwählen (eine Liste kann auf Basis des Endpunkts erstellt werden) [Get available carrier list](../api/globkurier.md#/Carriers/carrierListR01))
* für die Preisermittlung verwenden wir [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice) mit dem Parameter onlyPricing = true und geben collectionType als CROSSBORDER an
* Terminals / Punkte können für bestimmte Carrier über [Get shipment/receiving](../api/globkurier.md#/Points/pointGetList) abgerufen werden
* Nach korrekter/bestätigter Preisermittlung kann die Bestellung auf dieselbe Weise aufgegeben werden - onlyPricing = false, createFully = true

### Beispiel

.../v1/order/bestPrice?onlyPricing=true&createFully=false

Body Type : application/json

```json
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
```
