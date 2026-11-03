---
title: Labels
---

## Versandetikett herunterladen
Nach Aufgabe und Bezahlung der Bestellung erzeugt das System beim Carrier einen Auftrag, für den Sie über den Endpunkt [Get labels](../api/globkurier.md#/Order%20Documents/orderGetLabels) ein PDF-Etikett herunterladen können.

Der Endpunkt erfordert die Parameter: 

- `hash` - Bestellkennung. Der `Hash` wird auf zwei Wegen zurückgegeben:
    - bei der Aufgabe einer Bestellung (Endpunkt [Create order](../api/globkurier.md#/Orders/orderCreate) oder [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice)) werden in der Antwort die Bestellnummer und der Hash gesendet. 
    - beim Abruf der Bestelldaten (Endpunkt [Get order](../api/globkurier.md#/Orders/orderGetDetails) ) erhalten wir in der Antwort das Feld `hash`

- `format` - Etikettengröße: A4 / ZEBRA
