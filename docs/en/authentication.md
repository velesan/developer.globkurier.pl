---
title: Authentication
---

Protected resources require a token sent in the `X-Auth-Token` header.

| Step | Endpoint |
|---|---|
| Get a token with your GlobKurier.pl e-mail and password | [`POST /v1/auth/login`](api/globkurier.md#/Authentication/authLoginR01) |
| Extend the validity of the current token (the value stays the same) | [`POST /v1/auth/refresh`](api/globkurier.md#/Authentication/authRefreshR01) |
| Invalidate the current token | [`POST /v1/auth/logout`](api/globkurier.md#/Authentication/authLogoutR01) |

- `POST /v1/auth/login` accepts `application/json` or `application/x-www-form-urlencoded`; any other content type returns `415`.
- Call login **without** a valid token: an already authenticated caller gets `401`.
- `401` on a protected resource: the token is missing, invalid or expired. `403`: the token has no access to the resource.
- Some resources work without a token and return more data with one (e.g. product search).

```bash
curl -s https://test.api.globkurier.pl/v1/auth/login \
  -H 'Content-Type: application/json' \
  -d '{"email": "you@example.com", "password": "..."}'
# {"token": "..."}

curl -s https://test.api.globkurier.pl/v1/addresses -H 'X-Auth-Token: <token>'
```

!!! warning
    Never paste a token into a public issue. If one leaks, call `POST /v1/auth/logout` with it.
