---
title: Labels
---

#### Downloading a shipping label
After placing and paying for the order, the system will generate an order with the carrier for which you can download a PDF label via the endpoint [Get labels](../api/globkurier.md#/Order%20Documents/orderGetLabels)

Endpoint requires parameters: 
- `hash` - order ID. The `Hash` is returned in two ways:
   - when placing an order (endpoint [Create order](../api/globkurier.md#/Orders/orderCreate) or [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice)) in response, the order number and hash will be sent. 
   - when downloading order data (endpoint [Get order](../api/globkurier.md#/Orders/orderGetDetails) ) in response we will get the `hash` field

- `format` - label size: A4 / ZEBRA
