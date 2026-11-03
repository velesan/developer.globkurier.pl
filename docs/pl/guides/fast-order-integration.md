---
title: Fast order Integration
---

#### 1. Opis
Najszybszą metodą wybrania najkorzystniejszej oferty i złożenia zamówienia jest endpoint [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice). 

Jest to połączenie kilku punktów z [Full Integration (PL)](full-integration.md) w jeden. Zamiast odpytywać o wszystkie produkty, dodatki i dopiero składać zamówienie, to system sam znjadzie najlepszą (najtańszą) ofertę i weźmie ją do realizacji. 

Struktura endpoint jest zbliżona do endpoint'ów [Get products](../api/globkurier.md#/Products/productSearch), [Get order price](../api/globkurier.md#/Order%20Pricing/orderGetPrice) i [Create order](../api/globkurier.md#/Orders/orderCreate).

#### 2. Struktura
Można wykorzystać opis strategii [Full Integration (PL)](full-integration.md) do zbudowania zapytania, a kluczowe różnice to:
- w sekcji `shipment`:
  - nie ma `productId` (nie wskazujemy konkretnego produktu)
  - pojawia się `integrationName` - kod przewoźnika, którym chcemy wysłać przesyłkę. Kody można pobrać z endpoint opisanego tutaj: [Get carrier data (PL)](get-carrier-data.md) np. DPD, DHL 
- w sekcji `addons` podajemy kategorie usług dodatkowych (dodatków), które nas interesują do zamówienia wraz z przesyłką (lista: [Addon categories (PL)](addon-categories.md)) 
  np. "addons": {
        "INSURANCE": {
            "value": 100
        }}
 
#### 3. Działanie
System dla podanych parametrów, będzie starał sie znaleźć najtańszą ofertę spełniającą wszystkie warunki. Jeżeli w sekcji senderAddress podany zostanie pointId, to system będzie szukał oferty, która ma nadanie w punkcie (niekoniecznie z możliwym podjazdem kuriera -> zmiast zatem DPD, to wybrana zostanie opcja DPD Pickup). 

#### 4. Sterowanie działaniem
W adresie URL podając parametry createFully oraz onlyPricing decydujemy o rodzaju działania algorytmu:


| Parametr | Działanie |
| --- | --- |
| onlyPricing = true | System zwróci odpowiedź z wyliczonymi stawkami i z informacją o przypisanych dodatkach (analogicznie jak endpoint [Get order price](../api/globkurier.md#/Order%20Pricing/orderGetPrice)) |
| createFully = true | System utworzy automatycznie zlecenie zarówno w systemie Globkurier jak i przekaże do przewoźnika. Analogicznie jak endpoint [Create order](../api/globkurier.md#/Orders/orderCreate) |

#### 5. Błędy odpowiedzi
Istnieje kilka możliwych odpowiedzi systemu z powodu błędu:


| Odpowiedź | Wyjaśnienie |
| --- | --- |
|  "fields": {"addons[RETURN_SHIPMENT][id]": "This value is not available"} | Nie znajduje takiego dodatku dla podanych parametrów. Należy skasować wskazany dodatek. |
| {"fields": {"collectionType": "No product was found for the specified collection type."}} | Dla podanego rodzaju nadania nie znaleziono produktu (należy zmienić albo kuriera albo typ nadania) |
| {"fields": {"shipment[integrationName]": "This offer is not available for given carrier."}} | Nie ma żadnej oferty dla wybranego kuriera, typu nadania i typu dostawy |

#### 6. Odpowiedź prawidłowa
Po realizacji
