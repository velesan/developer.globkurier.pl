---
title: Get carrier data
---

#### 1. Dane o przewoźnikach i usługach
W celu pobrania wszystkich danych o przewoźniku (nazwy, kody integracyjne, możliwe dodatki), 
Endpoint: [Get available carrier list](../api/globkurier.md#/Carriers/carrierListR01)

Opcjonalne parametry wywołania:
- addonCategories[] - wyszukiwanie konkretnych kurierów obsługujących wskazane dodatki (AND)
- deliveryTypes[] - wyszukiwanie konkretnych kurierów obsługujących wskazane metody dostawy (OR)
- collectionTypes[] - wyszukiwanie konkretnych kurierów obsługujących wskazane metody nadania (OR)

Struktura odpowiedzi:
- nazwa integracyjna kuriera: `carrierName`
- link do logo: `logo`
- lista dostępnych kategorii usług dodatkowych - kod i nazwa: `addonCategories`
- kody serwisowe dla usług głównych: `serviceCodes`
- `deliveryTypes` - możliwe typy dostawy dla kuriera
- `collectionTypes` - możliwe typy nadania dla kuriera

#### 2. Dane o punktach przewoźnika
Punkty / oddziały / automaty pobrać można poprzez endpoint [Get shipment/receiving](../api/globkurier.md#/Points/pointGetList)

Punkty można pobrać dla dwóch scenariuszy:
- dla każdego produktu osobno (wypełniamy parametr `productId`)
- dla każdego przewoźnika +/- dla kodów serwisowych:
   - zwraca możliwe punkty do użycia
   - ustawiamy pola:`carrierName`,`serviceCode`
