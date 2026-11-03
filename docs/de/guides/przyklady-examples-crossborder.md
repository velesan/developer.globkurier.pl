---
title: Przykłady / Examples Crossborder
---

## I.  [Simplified order placement (bestprice)](../api/globkurier.md#/Orders/orderCreateBestPrice)	
## 1. Eurohermes:
a.	Deutschland
{
    "shipment": {
        "length": 1,
        "width": 1,
        "height": 1,
        "weight": 1,
        "quantity": 1,
        "integrationName": "DHL DE"
    },
    "senderAddress": {
        "name": "Testowy Nadawca",
        "city": "Testowe Miasto",
        "street": "Testowa Ulica",
        "houseNumber": "1x",
        "apartmentNumber": "2a",
        "postCode": "01-001",
        "country": "PL",
        "pointId": "ZGORZELEC",
        "phone": "123123123",
        "email": "testowy.nadawca@testowy.nadawca.pl",
        "contactPerson": "Testowa Osoba",
        "nip": "1234563218"
    },
    "receiverAddress": {
        "name": "Testowy Odbiorca",
        "city": "Testowe Miasto",
        "street": "Testowa Ulica",
        "houseNumber": "1x",
        "apartmentNumber": "2a",
        "postCode": "01001",
        "country": "DE",
        "phone": "123123123",
        "email": "testowy.odbiorca@testowy.odbiorca.pl",
        "contactPerson": "Testowa Osoba",
        "nip": "1234563218"
    },
    "content": "Książki / books",
    "paymentId": 4,
    "originId": "API",
    
    "declaredValue": "50",
    "purpose": "SOLD",
    "collectionType": "CROSSBORDER",
    "referenceNumber": "TEST/1234",
    "deliveryType": "PICKUP"
}

b.	Frankreich
{
    "shipment": {
        "length": 1,
        "width": 1,
        "height": 1,
        "weight": 1,
        "quantity": 1,
        "integrationName": "COLISSIMO"
    },
    "senderAddress": {
        "name": "Testowy Nadawca",
        "city": "Testowe Miasto",
        "street": "Testowa Ulica",
        "houseNumber": "1x",
        "apartmentNumber": "2a",
        "postCode": "01-001",
        "country": "PL",
        "pointId": "ZGORZELEC",
        "phone": "123123123",
        "email": "testowy.nadawca@testowy.nadawca.pl",
        "contactPerson": "Testowa Osoba",
        "nip": "1234563218"
    },
    "receiverAddress": {
        "name": "Testowy Odbiorca",
        "city": "Testowe Miasto",
        "street": "Testowa Ulica",
        "houseNumber": "1x",
        "apartmentNumber": "2a",
        "postCode": "01001",
        "country": "FR",
        "phone": "123123123",
        "email": "testowy.odbiorca@testowy.odbiorca.pl",
        "contactPerson": "Testowa Osoba",
        "nip": "1234563218"
    },
    "content": "Książki / Books",
    "paymentId": 4,
    "originId": "API",
    
    "declaredValue": "50",
    "purpose": "SOLD",
    "collectionType": "CROSSBORDER",
    "referenceNumber": "TEST/1234",
    "deliveryType": "PICKUP"
}

## 2.	Spring:
a.	Spanien, Deutschland, Portugal, Italien, Rumänien (EU): 
{
    "shipment": {
        "length": 1,
        "width": 1,
        "height": 1,
        "weight": 1,
        "quantity": 1,
        "integrationName": "Cross Border"
    },
    "senderAddress": {
        "name": "Testowy Nadawca",
        "city": "Testowe Miasto",
        "street": "Testowa Ulica",
        "houseNumber": "1x",
        "apartmentNumber": "2a",
        "postCode": "01-001",
        "country": "PL",
        "pointId": "WROCLAW",
        "phone": "123123123",
        "email": "testowy.nadawca@testowy.nadawca.pl",
        "contactPerson": "Testowa Osoba",
        "nip": "1234563218"
    },
    "receiverAddress": {
        "name": "Testowy Odbiorca",
        "city": "Testowe Miasto",
        "street": "Testowa Ulica",
        "houseNumber": "1x",
        "apartmentNumber": "2a",
        "postCode": "01001",
        "country": "ES",
        "phone": "123123123",
        "email": "testowy.odbiorca@testowy.odbiorca.pl",
        "contactPerson": "Testowa Osoba",
        "nip": "1234563218"
    },
    "content": "Książki / books",
    "paymentId": 4,
    "originId": "API",
    
    "declaredValue": "50",
    "purpose": "SOLD",
    "collectionType": "CROSSBORDER",
    "referenceNumber": "TEST/1234",
    "deliveryType": "PICKUP"
}

## 3.	UK – Spring

{
    "shipment": {
        "length": 1,
        "width": 1,
        "height": 1,
        "weight": 1,
        "quantity": 1,
        "integrationName": "Cross Border"
    },
    "senderAddress": {
        "name": "Testowy Nadawca",
        "city": "Testowe Miasto",
        "street": "Testowa Ulica",
        "houseNumber": "1x",
        "apartmentNumber": "2a",
        "postCode": "01-001",
        "country": "PL",
        "pointId": "WROCLAW",
        "phone": "123123123",
        "email": "testowy.nadawca@testowy.nadawca.pl",
        "contactPerson": "Testowa Osoba",
        "nip": "1234563218"
    },
    "receiverAddress": {
        "name": "Testowy Odbiorca",
        "city": "Testowe Miasto",
        "street": "Testowa Ulica",
        "houseNumber": "1x",
        "apartmentNumber": "2a",
        "postCode": "M2 1ST",
        "country": "GB",
        "phone": "123123123",
        "email": "testowy.odbiorca@testowy.odbiorca.pl",
        "contactPerson": "Testowa Osoba",
        "nip": "1234563218"
    },
    "content": "Książki / books",
    "paymentId": 4,
    "originId": "API",
    "declaredValue": "50",
    "purpose": "SOLD",
    "collectionType": "CROSSBORDER",
    "referenceNumber": "TEST/1234",
    "deliveryType": "PICKUP",
  "customs": {
    "currency": "PLN",
    "total": "150",
    "totalWeight": "5",
    "sender": {
      "eori": "PL.........."
    },
    "receiver": {
      "eori": "GB..........."
    },
    "commodities": [
      {
        "description": "Sponge blocks (castle)",
        "hsCode": "95069990",
        "countryOfOrigin": "PL",
        "quantity": "1",
        "unitValue": "150",
        "unitWeight": "5",
        "subTotalValue": "150"
      }
    ],
    "postalCharges": "0",
    "purpose": "SaleOfGoods",
    "vatRegistrationNumber": "PL...........",
    "vatRegistrationNumberReceiver": "GB...................."
  }
}
