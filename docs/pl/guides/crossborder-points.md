---
title: Crossborder / Points
---

# Działanie crossborder i punkty:
#### Wstęp
- Obsługa crossborder i punktów PUDO jest identyczna. 
- Crossborder jest dostepny o ile dany produkt występuje w cenniku dla klienta.
- CollectionType w endpoint /products powinien zawierać obiekt z tekstem CROSSBORDER lub POINT:
            "`collectionTypes`": ["CROSSBORDER"]
- w momencie wybrania tego produktu, miejsca nadania pobieramy poprzez endpoint /points dla `productId` = wybrany produkt wraz z pozostałymi parametrami - otrzymamy listę terminali / punktów. Alternatywnie zamiast `productId` można podać kod przewoźnika i otrzymamy pełną listę punktów ([Get carrier datas (PL)](get-carrier-data.md))
- wybrany terminal (id) / punkt (id) wstawiamy jako pointId w sekcji senderAddress.

#### Kurierzy dla Crossborder:
* DHL DE
* Balikovna
* POST NORD DIRECT LINK
* Royal Mail
* Spring

#### Dla pełnej integracji:
* /products - produkty dla kryteriów 
* /products/addons  - dodatki do wybranego produktu
* /points -> pobranie punktów dla produktu crossborder/point
* /order/price - przeliczenie całościowe zamówienia
* /order/validate - walidacja danych
* /order - zamawianie


#### Szybka ścieżka ([Fast order Integration (PL)](fast-order-integration.md)):
* należy udostępnić klientowi wybór kategorii usług dodatkowych (można listę stworzyć na podstawie endpointu [Get available carrier list](../api/globkurier.md#/Carriers/carrierListR01))
* dla wyceny wykorzystujemy [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice) z parametrem onlyPricing = true i dajemy collectionType jako CROSSBORDER
* terminale / punkty można pobrać poprzez [Get shipment/receiving](../api/globkurier.md#/Points/pointGetList) dla konkretnych przewoźników
* Po poprawnej / potwierdzeniu wyceny można złożyć zamówienie w identyczny sposób - onlyPricing = false, createFully = true

#### Przykład

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
