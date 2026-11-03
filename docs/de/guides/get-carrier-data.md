---
title: Get carrier data
---

## 1. Daten zu Carriern und Services
Um alle Carrier-Daten (Namen, Integrationscodes, mögliche Zusatzservices) abzurufen,
Endpunkt: [Get available carrier list](../api/globkurier.md#/Carriers/carrierListR01)

Optionale Aufrufparameter:

- addonCategories[] - Suche nach bestimmten Carriern, die die angegebenen Zusatzservices unterstützen (AND)
- deliveryTypes[] - Suche nach bestimmten Carriern, die die angegebenen Zustellarten unterstützen (OR)
- collectionTypes[] - Suche nach bestimmten Carriern, die die angegebenen Versandarten unterstützen (OR)

Struktur der Antwort:

- Integrationsname des Carriers: `carrierName`
- Link zum Logo: `logo`
- Liste der verfügbaren Zusatzservice-Kategorien - Code und Name: `addonCategories`
- Servicecodes für die Hauptservices: `serviceCodes`
- `deliveryTypes` - mögliche Zustellarten für den Carrier
- `collectionTypes` - mögliche Versandarten für den Carrier

## 2. Daten zu Carrier-Punkten
Punkte/Filialen/Automaten können über den Endpunkt [Get shipment/receiving](../api/globkurier.md#/Points/pointGetList) abgerufen werden

Punkte können für zwei Szenarien abgerufen werden:

- für jedes Produkt einzeln (wir füllen den Parameter `productId` aus)
- für jeden Carrier +/- nach Servicecodes:
    - liefert mögliche nutzbare Punkte
    - wir setzen die Felder: `carrierName`, `serviceCode`
