---
title: Authentifizierung
---

Geschützte Ressourcen erfordern ein Token, das im Header `X-Auth-Token` gesendet wird.

| Schritt | Endpunkt |
|---|---|
| Token mit Ihrer GlobKurier.pl-E-Mail-Adresse und Ihrem Passwort abrufen | [`POST /v1/auth/login`](api/globkurier.md#/Authentication/authLoginR01) |
| Gültigkeit des aktuellen Tokens verlängern (der Wert bleibt gleich) | [`POST /v1/auth/refresh`](api/globkurier.md#/Authentication/authRefreshR01) |
| Das aktuelle Token ungültig machen | [`POST /v1/auth/logout`](api/globkurier.md#/Authentication/authLogoutR01) |

- `POST /v1/auth/login` akzeptiert `application/json` oder `application/x-www-form-urlencoded`; jeder andere Content-Type liefert `415`.
- Rufen Sie login **ohne** gültiges Token auf: Ein bereits authentifizierter Aufrufer erhält `401`.
- `401` bei einer geschützten Ressource: Das Token fehlt, ist ungültig oder abgelaufen. `403`: Das Token hat keinen Zugriff auf die Ressource.
- Einige Ressourcen funktionieren ohne Token und liefern mit Token mehr Daten (z. B. die Produktsuche).

```bash
curl -s https://test.api.globkurier.pl/v1/auth/login \
  -H 'Content-Type: application/json' \
  -d '{"email": "you@example.com", "password": "..."}'
# {"token": "..."}

curl -s https://test.api.globkurier.pl/v1/addresses -H 'X-Auth-Token: <token>'
```

!!! warning "Achtung"
    Fügen Sie niemals ein Token in ein öffentliches Issue ein. Falls eines offengelegt wird, rufen Sie `POST /v1/auth/logout` damit auf.
