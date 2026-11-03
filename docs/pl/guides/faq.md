---
title: FAQ
---

## 1. Jak wygenerować z zamówieniem etykietę zwrotną:
* dla integracji [Full Integration (PL)](full-integration.md) należy wybrac dodatek z kategorii `RETURN_SHIPMENT`
* dla integracji [Fast order Integration (PL)](fast-order-integration.md) w sekcji addons podajemy wprost kategorię: `"RETURN_SHIPMENT":{"value": true}`.


W obu integracjach po złożeniu zamówienia w odpowiedzi dostaniemy linki do etykiety głównej i zwrotnej - mogą być opóźnienia po stronie przewoźnika w generowaniu etykiety zwrotnej. Dlatego warto ponowić wtedy żądanie i wywołać endpoint [Get order](../api/globkurier.md#/Orders/orderGetDetails).

Odpowiedzi:

- informacja o numerach zwrotnych:

    ```json
    "returnShipment": {
        "number": null,
        "trackingNumber": null
    }
    ```

- linki do etykiet:

    ```json
    "transportDocuments": [],
    ```
