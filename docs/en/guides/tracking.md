---
title: Tracking
---

## 1. To download the history and current status of your order, download via endpoint: [Get shipment statuses](../api/globkurier.md#/Order%20Tracking/orderGetTracking).
## 2. Data can only be downloaded for shipments sent from the Globkurier system. The number must begin with GK....
## 3. Authorization:

- without `x-auth-token` - system will return statuses without address data
- with `x-auth-token`, to which the order relates will also return the address details
## 4. Response

- current status:`latestStatus`
- history arranged by ascending date:`statuses`
