---
title: Pricing Summary before ordering
---

## Bestellübersicht
Vor der Aufgabe Ihrer Bestellung können Sie die vollständige Abrechnung der Bestellung samt Prüfung des Rabattcodes abrufen. 

Dafür verwenden wir den Endpunkt [Get order price](../api/globkurier.md#/Order%20Pricing/orderGetPrice). 
Der Endpunkt akzeptiert ähnliche Parameter wie der Endpunkt zur Bestellaufgabe [Create order](../api/globkurier.md#/Orders/orderCreate). Bitte übergeben Sie alle vom Kunden angegebenen Daten.
Anstatt die Sendungsparameter im body-Abschnitt anzugeben, senden wir sie als Parameter in der URL.
Als Antwort erhalten wir detaillierte Informationen zur Abrechnung der Bestellung:

| Feld | Beschreibung |
|------|--------------|
| `currency` | WÄHRUNG |
| `taxType` | MwSt.-Art |
| `vatPercent` | MwSt.-Satz |
| `totalGrossPrice` | Gesamtbetrag brutto |
| `totalNetPrice` | Gesamtbetrag netto |
| `netPriceWithoutFuelSurcharge` | Nettobetrag ohne Treibstoffzuschlag |
| `productNetPrice` | Nettobetrag des Produkts |
| `productsNetPrice` | Summe der Nettobeträge für das Produkt mit Rabatt |
| `productsGrossPrice` | Summe der Bruttobeträge für das Produkt mit Rabatt |
| `productsStockNetPrice` | Summe der Nettobeträge für das Produkt ohne Rabatt |
| `productsStockGrossPrice` | Summe der Bruttobeträge für das Produkt ohne Rabatt |
| `fuelSurchargeNetPrice` | Treibstoffzuschlag mit Rabatt - netto |
| `fuelSurchargeGrossPrice` | Treibstoffzuschlag mit Rabatt - brutto |
| `fuelSurcharge` | Treibstoffgebühr - veraltetes Feld |
| `fuelSurchargeStockNetPrice` | Treibstoffzuschlag ohne Rabatt - netto |
| `fuelSurchargeStockGrossPrice` | Treibstoffzuschlag ohne Rabatt - brutto |
| `addonsNetPrice` | Nettobetrag für Zusatzservices |
| `addonsGrossPrice` | Bruttobetrag für Zusatzservices |
| `discountNetPrice` | angewandter Rabattbetrag |
| `packages[]` | Liste der Sendungsbestandteile. |
| `addons[]` | Liste der Zusatzservices, die Netto- (price) und Bruttobeträge (proceGross) nach Berechnung des Rabatts ausweisen |
