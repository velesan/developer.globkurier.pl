---
title: Shipment search
---

## 1. Punkt -> Punkt

W celu wyszukania transportu pomiędzy punktami (ATM/PUDO) należy posłużyć się wyszukiwaniem ofert używając pól:
    
| Endpoint | Nazwa | Wartość | Link |
| --- | --- | --- | --- |
| /order | collectionType | POINT | [Create order](../api/globkurier.md#/Orders/orderCreate) |
| /order | deliveryType | POINT | [Create order](../api/globkurier.md#/Orders/orderCreate) |
| /order/bestPrice | collectionType | POINT | [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice) |
| /order/bestPrice | deliveryType | POINT | [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice) |
| /products | collectionTypes | POINT | [Pobranie produktów](../api/globkurier.md#/Products/productSearch) |
| /products | deliveryTypes | POINT | [Pobranie produktów](../api/globkurier.md#/Products/productSearch) |

Nie ma wymagania podawania punktu nadawczego, ale w przypadku odbioru wymagane jest pole receiverAddress[pointId].

## 2. Punkt -> Drzwi

W celu wyszukania transportu z punktu (ATM/PUDO) należy posłużyć się wyszukiwaniem ofert używając pól:
    
| Endpoint | Nazwa | Wartość | Link |
| --- | --- | --- | --- |
| /order | collectionType | POINT | [Create order](../api/globkurier.md#/Orders/orderCreate) |
| /order | deliveryType | PICKUP | [Create order](../api/globkurier.md#/Orders/orderCreate) |
| /order/bestPrice | collectionType | POINT | [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice) |
| /order/bestPrice | deliveryType | PICKUP | [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice) |
| /products | collectionTypes | POINT | [Pobranie produktów](../api/globkurier.md#/Products/productSearch) |
| /products | deliveryTypes | PICKUP | [Pobranie produktów](../api/globkurier.md#/Products/productSearch) |

Czy punkt jest wymagany, zależy od produktu: sprawdź `senderAddressPointId` / `receiverAddressPointId` w [Get custom required fields](../api/globkurier.md#/Orders/orderGetCustomRequiredFields).

## 3. Crossborder -> Drzwi

       
| Endpoint | Nazwa | Wartość | Link |
| --- | --- | --- | --- |
| /order | collectionType | CROSSBORDER | [Create order](../api/globkurier.md#/Orders/orderCreate) |
| /order | deliveryType | PICKUP | [Create order](../api/globkurier.md#/Orders/orderCreate) |
| /order/bestPrice | collectionType | CROSSBORDER | [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice) |
| /order/bestPrice | deliveryType | PICKUP | [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice) |
| /products | collectionTypes | CROSSBORDER | [Pobranie produktów](../api/globkurier.md#/Products/productSearch) |
| /products | deliveryTypes | PICKUP | [Pobranie produktów](../api/globkurier.md#/Products/productSearch) |

Produkty crossborder zwykle wymagają terminala nadawczego (`pointId`, z [Get carrier datas (PL)](get-carrier-data.md)). Czy punkt jest wymagany, zależy od produktu: sprawdź `senderAddressPointId` / `receiverAddressPointId` w [Get custom required fields](../api/globkurier.md#/Orders/orderGetCustomRequiredFields).
