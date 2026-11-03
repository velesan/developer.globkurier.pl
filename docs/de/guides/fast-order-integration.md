---
title: Fast order Integration
---

#### 1. Beschreibung
Der schnellste Weg, das beste Angebot auszuwählen und eine Bestellung aufzugeben, führt über den Endpunkt [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice). 

Er fasst mehrere Punkte aus [Full Integration (DE)](full-integration.md) in einem zusammen. Statt nach allen Produkten und Zusatzservices zu fragen und anschließend die Bestellung aufzugeben, findet das System automatisch das beste (günstigste) Angebot und führt es aus. 

Die Struktur des Endpunkts ähnelt den Endpunkten [Get products](../api/globkurier.md#/Products/productSearch), [Get order price](../api/globkurier.md#/Order%20Pricing/orderGetPrice) und [Create order](../api/globkurier.md#/Orders/orderCreate).

#### 2. Struktur
Sie können die Strategiebeschreibung [Full Integration (DE)](full-integration.md) nutzen, um eine Anfrage aufzubauen; die wesentlichen Unterschiede sind:
- im Abschnitt `shipment`:
  - es gibt kein `productId` (wir geben kein bestimmtes Produkt an)
  - es erscheint `integrationName` - der Code des Carriers, mit dem wir die Sendung versenden möchten. Die Codes können über den hier beschriebenen Endpunkt abgerufen werden: [Get carrier data (DE)](get-carrier-data.md) z. B. DPD, DHL 
- im Abschnitt `addons` geben wir die Kategorien der Zusatzservices (add-ons) an, die wir zusammen mit der Sendung bestellen möchten (Liste: [Addon categories (DE)](addon-categories.md)) 
  z. B. "addons": {
        "INSURANCE": {
            "value": 100
        }}
 
#### 3. Ablauf
Für die angegebenen Parameter versucht das System, das günstigste Angebot zu finden, das alle Anforderungen erfüllt. Wird im Abschnitt senderAddress ein pointId angegeben, sucht das System ein Angebot, das von einem Punkt aus versendet wird (nicht unbedingt mit Abholung durch einen Kurier -> statt DPD wird die Option DPD Pickup gewählt).

#### 4. Steuerung des Vorgangs
Durch Angabe der Parameter createFully und onlyPricing in der URL entscheiden wir, welcher Algorithmus verwendet wird:

| Parameter | Aktion |
| --- | --- |
| onlyPricing = true | Das System liefert eine Antwort mit berechneten Preisen und Informationen über zugewiesene Rabatte (ähnlich wie beim Endpunkt [Get order price](../api/globkurier.md#/Order%20Pricing/orderGetPrice)) |
| createFully = true | Das System erstellt die Bestellung automatisch sowohl im Globkurier-System als auch beim Carrier. Ähnlich wie beim Endpunkt [Create order](../api/globkurier.md#/Orders/orderCreate) |

#### 5. Fehlerantworten
Aufgrund eines Fehlers sind mehrere Antworten des Systems möglich:

| Antwort | Erläuterung |
| --- | --- |
|  "fields": {"addons[RETURN_SHIPMENT][id]": "This value is not available"} | Für die angegebenen Parameter wurde kein solcher Zusatzservice gefunden. Der angegebene Zusatzservice sollte entfernt werden |
| {"fields": {"collectionType": "No product was found for the specified collection type."}} | Für die angegebene Versandart wurde kein Produkt gefunden (es muss entweder der Kurier oder die Versandart geändert werden) |
| {"fields": {"shipment[integrationName]": "This offer is not available for given carrier."}} | Für den gewählten Kurier, die Versandart und die Zustellart gibt es keine Angebote |

#### 6. Korrekte Antwort
Nach der Implementierung
