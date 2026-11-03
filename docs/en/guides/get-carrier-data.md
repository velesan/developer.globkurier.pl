---
title: Get carrier data
---

#### 1. Data on carriers and services
To download all carrier data (names, integration codes, possible additions), 
Endpoint: [Get available carrier list](../api/globkurier.md#/Carriers/carrierListR01)

Optional call parameters:
- addonCategories[] - search for specific couriers supporting the specified add-ons (AND)
- deliveryTypes[] - search for specific couriers supporting the specified delivery methods (OR)
- collectionTypes[] - search for specific couriers supporting the specified shipping methods (OR)

Response structure:
- courier integration name: `carrierName`
- logo link: `logo`
- list of available additional service categories - code and name: `addonCategories`
- service codes for main services: `serviceCodes`
- `deliveryTypes` - possible delivery types for the courier
- `collectionTypes` - possible shipping types for the courier

#### 2. Data on carrier points
Points/branches/automat can be downloaded via endpoint [Get shipment/receiving](../api/globkurier.md#/Points/pointGetList)

Points can be collected for two scenarios:
- for each product separately (we fill in the `productId` parameter)
- for each carrier +/- for service codes:
   - returns possible points to use
   - we set the fields: `carrierName`, `serviceCode`
