---
title: FAQ
---

## 1. How to generate a return label with your order:
* for integration [Full Integration (EN)](full-integration.md) you must select an add-on from the `RETURN_SHIPMENT` category
* for integration [Fast order Integration (EN)](fast-order-integration.md) in the addons section we provide the category directly: `"RETURN_SHIPMENT":{"value": true}`.

In both integrations, after placing an order, we'll receive links to the main and return labels in response. There may be delays on the carrier's side in generating the return label. Therefore, it's worth repeating the request and calling the endpoint [Get order](../api/globkurier.md#/Orders/orderGetDetails).

Answers:

- information about return numbers:

    ```json
    "returnShipment": {
        "number": null,
        "trackingNumber": null
    }
    ```

- links to labels:

    ```json
    "transportDocuments": [],
    ```
