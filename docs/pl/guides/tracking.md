---
title: Tracking
---

## 1. W celu pobierania historii i aktualnego statusu zamówienia należy pobierać poprzez endpoint: [Get shipment statuses](../api/globkurier.md#/Order%20Tracking/orderGetTracking).
## 2. Dane można pobierać tylko dla przesyłek wysyłanych z systemu Globkurier. Numer musi zaczynać się od GK....
## 3. Autoryzacja:

- bez `x-auth-token` - system zwróci statusy bez danych adresowych
- z `x-auth-token`, którego dotyczy zamówienie zwróci również dane adresowe.
## 4. Odpowiedź

- aktualny status:`latestStatus`
- historia ułożona wg daty rosnącej:`statuses`
