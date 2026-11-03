---
title: Pricing Summary before ordering
---

## Podsumowanie zamówienia
Przed złożeniem zamówienia można pobrać całkowite rozliczenie zamówienia wraz z weryfikacją kodu rabatowych. 

Wykorzystujemy do tego endpoint [Get order price](../api/globkurier.md#/Order%20Pricing/orderGetPrice). 
Endpoint przyjmuje podobne parametry co endpoint do składania zamówienia [Create order](../api/globkurier.md#/Orders/orderCreate). Należy podać wszystkie dane, które wskazał klient. 
Zamiast parametry przesyłki dawać w sekcji body, wysyłamy w URL jako parametry.
Zwrotnie otrzymamy szczegółowe dane związane z rozliczeniem zamówienia:

| Pole | Opis |
|------|------|
| `currency` | WALUTA |
| `taxType` | typ VAT |
| `vatPercent` | Stawka VAT |
| `totalGrossPrice` | całkowita kwota brutto |
| `totalNetPrice` | całkowita kwota netto |
| `netPriceWithoutFuelSurcharge` | kwota netto bez opłaty paliwowej |
| `productNetPrice` | kwota netto produktu |
| `productsNetPrice` | suma kwot netto za produkt z rabatem |
| `productsGrossPrice` | suma kwot brutto za produkt z rabatem |
| `productsStockNetPrice` | suma kwot netto za produkt bez rabatu |
| `productsStockGrossPrice` | suma kwot brutto za produkt bez rabatu |
| `fuelSurchargeNetPrice` | opłata paliwowa z rabatem - netto |
| `fuelSurchargeGrossPrice` | opłata paliwowa z rabatem - brutto |
| `fuelSurcharge` | opłata paliwowa - wycofywane pole |
| `fuelSurchargeStockNetPrice` | opłata paliwowa bez rabatu - netto |
| `fuelSurchargeStockGrossPrice` | opłata paliwowa bez rabatu - brutto |
| `addonsNetPrice` | kwota netto za dodatki |
| `addonsGrossPrice` | kwota brutto za dodatki |
| `discountNetPrice` | kwota rabatu naliczonego |
| `packages[]` | Lista składowych przesyłek. |
| `addons[]` | Lista dodatków, które prezentują kwoty netto (price) i brutto (priceGross) po przeliczeniu rabatu |
