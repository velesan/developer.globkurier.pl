---
title: Shipment search
---

## 1. Point -> Point

To search for transport between points (ATM/PUDO), use the offer search box:
    
| Endpoint | Name | Value | Link |
| --- | --- | --- | --- |
| /order | collectionType | POINT | [Create order](../api/globkurier.md#/Orders/orderCreate) |
| /order | deliveryType | POINT | [Create order](../api/globkurier.md#/Orders/orderCreate) |
| /order/bestPrice | collectionType | POINT | [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice) |
| /order/bestPrice | deliveryType | POINT | [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice) |
| /products | collectionTypes | POINT | [Get products](../api/globkurier.md#/Products/productSearch) |
| /products | deliveryTypes | POINT | [Get products](../api/globkurier.md#/Products/productSearch) |

There is no requirement to specify the sending point, but in case of reception the field receiverAddress[pointId] is required.

## 2. Point -> Door

To search for transport from a point (ATM/PUDO), use the offer search box:
    
| Endpoint | Name | Value | Link |
| --- | --- | --- | --- |
| /order | collectionType | POINT | [Create order](../api/globkurier.md#/Orders/orderCreate) |
| /order | deliveryType | PICKUP | [Create order](../api/globkurier.md#/Orders/orderCreate) |
| /order/bestPrice | collectionType | POINT | [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice) |
| /order/bestPrice | deliveryType | PICKUP | [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice) |
| /products | collectionTypes | POINT | [Get products](../api/globkurier.md#/Products/productSearch) |
| /products | deliveryTypes | PICKUP | [Get products](../api/globkurier.md#/Products/productSearch) |

Whether a pickup point is required depends on the product: check `senderAddressPointId` / `receiverAddressPointId` in [Get custom required fields](../api/globkurier.md#/Orders/orderGetCustomRequiredFields).

## 3. Crossborder -> Doors

       
| Endpoint | Name | Value | Link |
| --- | --- | --- | --- |
| /order | collectionType | CROSSBORDER | [Create order](../api/globkurier.md#/Orders/orderCreate) |
| /order | deliveryType | PICKUP | [Create order](../api/globkurier.md#/Orders/orderCreate) |
| /order/bestPrice | collectionType | CROSSBORDER | [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice) |
| /order/bestPrice | deliveryType | PICKUP | [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice) |
| /products | collectionTypes | CROSSBORDER | [Get products](../api/globkurier.md#/Products/productSearch) |
| /products | deliveryTypes | PICKUP | [Get products](../api/globkurier.md#/Products/productSearch) |

Crossborder products usually require the sender terminal (`pointId`, taken from [Get carrier datas (EN)](get-carrier-data.md)). Whether a pickup point is required depends on the product: check `senderAddressPointId` / `receiverAddressPointId` in [Get custom required fields](../api/globkurier.md#/Orders/orderGetCustomRequiredFields).
