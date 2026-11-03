---
title: Autoryzacja
---

Chronione zasoby wymagają tokenu w nagłówku `X-Auth-Token`.

| Krok | Endpoint |
|---|---|
| Pobierz token, podając e-mail i hasło do GlobKurier.pl | [`POST /v1/auth/login`](api/globkurier.md#/Authentication/authLoginR01) |
| Przedłuż ważność bieżącego tokenu (wartość się nie zmienia) | [`POST /v1/auth/refresh`](api/globkurier.md#/Authentication/authRefreshR01) |
| Unieważnij bieżący token | [`POST /v1/auth/logout`](api/globkurier.md#/Authentication/authLogoutR01) |

- `POST /v1/auth/login` przyjmuje `application/json` albo `application/x-www-form-urlencoded`; inny typ treści zwraca `415`.
- Logowanie wywołuj **bez** ważnego tokenu: zalogowany wywołujący dostaje `401`.
- `401` na chronionym zasobie: brak tokenu, token nieprawidłowy albo wygasły. `403`: token nie ma dostępu do zasobu.
- Część zasobów działa bez tokenu, a z tokenem zwraca więcej danych (np. wyszukiwanie produktów).

```bash
curl -s https://test.api.globkurier.pl/v1/auth/login \
  -H 'Content-Type: application/json' \
  -d '{"email": "ty@example.com", "password": "..."}'
# {"token": "..."}

curl -s https://test.api.globkurier.pl/v1/addresses -H 'X-Auth-Token: <token>'
```

!!! warning "Uwaga"
    Nigdy nie wklejaj tokenu do publicznego zgłoszenia. Jeśli wyciekł, wywołaj z nim `POST /v1/auth/logout`.
