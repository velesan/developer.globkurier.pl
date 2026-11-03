---
title: Shipment search
---

## 1. Punkt -> Punkt

Um nach Transporten zwischen Punkten (Automat/PUDO) zu suchen, verwenden Sie das Angebotssuchfeld:
    
| Endpunkt | Name | Wert | Link |
| --- | --- | --- | --- |
| /order | collectionType | POINT | [Create order](../api/globkurier.md#/Orders/orderCreate) |
| /order | deliveryType | POINT | [Create order](../api/globkurier.md#/Orders/orderCreate) |
| /order/bestPrice | collectionType | POINT | [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice) |
| /order/bestPrice | deliveryType | POINT | [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice) |
| /products | collectionTypes | POINT | [Get products](../api/globkurier.md#/Products/productSearch) |
| /products | deliveryTypes | POINT | [Get products](../api/globkurier.md#/Products/productSearch) |

Die Angabe des Versandpunkts ist nicht erforderlich, beim Empfang ist jedoch das Feld receiverAddress[pointId] erforderlich.

## 2. Punkt -> Tür

Um nach Transporten von einem Punkt (Automat/PUDO) zu suchen, verwenden Sie das Angebotssuchfeld:
    
| Endpunkt | Name | Wert | Link |
| --- | --- | --- | --- |
| /order | collectionType | POINT | [Create order](../api/globkurier.md#/Orders/orderCreate) |
| /order | deliveryType | PICKUP | [Create order](../api/globkurier.md#/Orders/orderCreate) |
| /order/bestPrice | collectionType | POINT | [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice) |
| /order/bestPrice | deliveryType | PICKUP | [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice) |
| /products | collectionTypes | POINT | [Get products](../api/globkurier.md#/Products/productSearch) |
| /products | deliveryTypes | PICKUP | [Get products](../api/globkurier.md#/Products/productSearch) |

Ob ein Paketpunkt erforderlich ist, hängt vom Produkt ab: prüfen Sie `senderAddressPointId` / `receiverAddressPointId` in [Get custom required fields](../api/globkurier.md#/Orders/orderGetCustomRequiredFields).

## 3. Crossborder -> Türen

       
| Endpunkt | Name | Wert | Link |
| --- | --- | --- | --- |
| /order | collectionType | CROSSBORDER | [Create order](../api/globkurier.md#/Orders/orderCreate) |
| /order | deliveryType | PICKUP | [Create order](../api/globkurier.md#/Orders/orderCreate) |
| /order/bestPrice | collectionType | CROSSBORDER | [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice) |
| /order/bestPrice | deliveryType | PICKUP | [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice) |
| /products | collectionTypes | CROSSBORDER | [Get products](../api/globkurier.md#/Products/productSearch) |
| /products | deliveryTypes | PICKUP | [Get products](../api/globkurier.md#/Products/productSearch) |

Crossborder-Produkte erfordern in der Regel das Absender-Terminal (`pointId`, aus [Get carrier datas (DE)](get-carrier-data.md)). Ob ein Paketpunkt erforderlich ist, hängt vom Produkt ab: prüfen Sie `senderAddressPointId` / `receiverAddressPointId` in [Get custom required fields](../api/globkurier.md#/Orders/orderGetCustomRequiredFields).
