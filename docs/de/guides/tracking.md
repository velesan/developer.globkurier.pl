---
title: Tracking
---

## 1. Um den Verlauf und den aktuellen Status Ihrer Bestellung abzurufen, verwenden Sie den Endpunkt: [Get shipment statuses](../api/globkurier.md#/Order%20Tracking/orderGetTracking).
## 2. Daten können nur für Sendungen abgerufen werden, die aus dem Globkurier-System versendet wurden. Die Nummer muss mit GK.... beginnen.
## 3. Autorisierung:

- ohne `x-auth-token` - das System liefert Status ohne Adressdaten
- mit `x-auth-token`, dem die Bestellung zugeordnet ist, liefert es zusätzlich die Adressdaten
## 4. Antwort

- aktueller Status: `latestStatus`
- Verlauf in aufsteigender Datumsreihenfolge: `statuses`
