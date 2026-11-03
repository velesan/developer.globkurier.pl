---
title: Labels
---

#### Pobieranie etykiety transportowej
Po złożeniu i opłaceniu zamówienia system wygeneruje zamówienie u przewoźnika, dla którego można pobrać etykietę PDF poprzez endpoint [Get labels](../api/globkurier.md#/Order%20Documents/orderGetLabels)

Endpoint wymaga podania parametrów: 
- `hash` - identyfikator zamówienia. `Hash` zwracany jest na dwa sposoby:
   - przy składaniu zamówienia (endpoint [Create order](../api/globkurier.md#/Orders/orderCreate) lub [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice)) w odpowiedzi przesłany zostanie numer zamówienia i hash. 
   - przy pobraniu danych zamówienia (endpoint [Get order](../api/globkurier.md#/Orders/orderGetDetails) ) w odpowiedzi uzyskamy pole `hash`

- `format` - rozmiar etykiety: A4 / ZEBRA
