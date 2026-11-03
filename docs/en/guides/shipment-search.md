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

There is no requirement to provide a shipping point.

## 3. Crossborder -> Doors

       
| Endpoint | Name | Value | Link |
| --- | --- | --- | --- |
| /order | collectionType | CROSSBORDER | [Create order](../api/globkurier.md#/Orders/orderCreate) |
| /order | deliveryType | PICKUP | [Create order](../api/globkurier.md#/Orders/orderCreate) |
| /order/bestPrice | collectionType | CROSSBORDER | [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice) |
| /order/bestPrice | deliveryType | PICKUP | [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice) |
| /products | collectionTypes | CROSSBORDER | [Get products](../api/globkurier.md#/Products/productSearch) |
| /products | deliveryTypes | PICKUP | [Get products](../api/globkurier.md#/Products/productSearch) |

PointId is required - crossborder terminal (ID is taken from the courier endpoint) [Get carrier datas (EN)](get-carrier-data.md))
