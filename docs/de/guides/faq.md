---
title: FAQ
---

## 1. So erzeugen Sie mit Ihrer Bestellung ein Retourenetikett:
* bei der Integration [Full Integration (DE)](full-integration.md) müssen Sie einen Zusatzservice aus der Kategorie `RETURN_SHIPMENT` auswählen
* bei der Integration [Fast order Integration (DE)](fast-order-integration.md) geben wir im Abschnitt addons die Kategorie direkt an: `"RETURN_SHIPMENT":{"value": true}`.

Bei beiden Integrationen erhalten wir nach der Bestellung in der Antwort Links zum Haupt- und zum Retourenetikett. Beim Carrier kann es zu Verzögerungen bei der Erzeugung des Retourenetiketts kommen. Daher lohnt es sich, die Anfrage zu wiederholen und den Endpunkt [Get order](../api/globkurier.md#/Orders/orderGetDetails) aufzurufen.

Antworten:

- Informationen zu den Retourennummern:

    ```json
    "returnShipment": {
        "number": null,
        "trackingNumber": null
    }
    ```

- Links zu den Etiketten:

    ```json
    "transportDocuments": [],
    ```
