---
title: Introduction
---

## 1. Rozpoczęcie pracy
API GlobKurier jest oparte o architekturę REST. Odpowiedź zwracana jest w formacie JSON. Komunikacja z produkcyjną końcówką jest szyfrowana w SSL.

Środowiska są rozdzielone. Do korzystania z API testowego wymagane jest posiadanie konta użytkownika produkcyjnego pod warunkiem, że minął dzień od rejestracji bądź aktualizacji profilu (czas propagacji na serwis testowy). Dane testowe ulegają usunięciu na koniec dnia.

Istnieje możliwość wysłania zapytania w formacie JSON z nagłówkiem Content-Type o wartości application/json. W innych przypadkach dla zapytań POST nagłówek ten powinien mieć wartość application/x-www-form-urlencoded.

Dla ułatwienia procesu integracji oraz testowania działania API dokumentacja zawiera interaktywne zapytania.

URL bazowy:
```
https://api.globkurier.pl/v1
```

URL testowy:
```
https://test.api.globkurier.pl/v1
```
## 2. Wersje językowe
Język API wybieramy przesyłając w nagłówku żądania `accept-language` kodu języka w standardzie ISO 639-1.

Obecnie wspierane języki:

- en (domyślny)
- pl
- br, cn, cz, de, es, fr, pt, ru

## 3. Typy zasobów
Wyróżniamy 3 typy zasobów ze względu na autoryzację:

- nie wymagające autoryzacji (np. pobranie listy krajów)
- z opcjonalną autoryzacją (np. wyszukiwarka produktów, która zwróci inne produkty dla gościa, a inne dla zalogowanego użytkownika) oznaczone w dokumentacji ikoną filtra 
- wymagające autoryzacji poprzez token

## 4. Odkrywanie zasobów
Dostępne metody możemy pozyskać odpytując dowolny zasób metodą HTTP OPTIONS. Odpowiedź będzie zawierała klucze w nagłówku:

- `Access-Control-Allow-Methods` - dozwolone metody HTTP zasobu np. OPTIONS, GET
- `Access-Control-Allow-Headers` - dozwolone nagłówki zasobu np. `x-auth-token`, `accept-language`, `x-currency`

Pozwala to na wcześniejszą weryfikację, czy dany zasób posiada dostęp niewymagający tokenu lub posiadany token uprawnia do niego.
Próba odpytania zasobu niedozwoloną metodą zakończy się statusem błędu `405 Method Not Allowed`.

## 5. Stałe używane w API
Lista zawiera stałe wartości, które należy w określonych przypadkach przekazać w żądaniu, a których nie można pobrać z zasobów API.

<table class="table table-striped table-bordered">
                    <thead>
                    <tr>
                        <th>Nazwa</th>
                        <th>Możliwe wartości</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>Typ nadania</td>
                        <td>
                            <code>PICKUP</code>,
                            <code>POINT</code>,
                            <code>CROSSBORDER</code>
                        </td>
                    </tr>
                    <tr>
                        <td>Typ odbioru</td>
                        <td>
                            <code>PICKUP</code>,
                            <code>POINT</code>,
                            <code>CROSSBORDER</code>
                        </td>
                    </tr>
                    <tr>
                        <td>Etykiety informacyjne</td>
                        <td>
                            <ul>
                                <li>
                                    typ transportu: <code>GROUND</code>,
                                    <code>AIR</code>
                                </li>
                                <li>
                                    dodatkowe informacje o przewoźniku: <code>PACZKOMAT</code>,
                                    <code>PACZKA_W_RUCHU</code>
                                </li>
                            </ul>
                        </td>
                    </tr>
                    <tr>
                        <td>Typ klienta</td>
                        <td>
                            <code>PERSON</code>,
                            <code>COMPANY</code>
                        </td>
                    </tr>
                    <tr>
                        <td>Cel przesyłki</td>
                        <td>
                            <code>SOLD</code>,
                            <code>GIFT</code>,
                            <code>SAMPLE</code>,
                            <code>NOT_SOLD</code>,
                            <code>PERSONAL_EFFECTS</code>,
                            <code>REPAIR_AND_RETURN</code>
                        </td>
                    </tr>
                    <tr>
                        <td>Status zamówienia</td>
                        <td>
                            <ul>
                                <li>
                                    <code>NEW_SHIPMENT</code> - nowe
                                </li>
                                <li>
                                    <code>IN_PROGRESS</code> - w trakcie przetwarzania przez system
                                </li>
                                <li>
                                    <code>IN_TRANSIT</code> - w trakcie realizacji przez przewoźnika
                                </li>
                                <li>
                                    <code>DELIVERED</code> - dostarczone
                                </li>
                                <li>
                                    <code>CANCELED</code> - anulowane
                                </li>
                                <li>
                                    <code>RETURNED_TO_SENDER</code> - zwrócone do nadawcy
                                </li>
                            </ul>
                        </td>
                    </tr>
                    <tr>
                        <td>Typ dokumentu finansowego</td>
                        <td>
                            <ul>
                                <li>
                                    <code>PROFORMA_INVOICE</code> - faktura proforma
                                </li>
                                <li>
                                    <code>INVOICE</code> - faktura VAT
                                </li>
                                <li>
                                    <code>CORRECTION_INVOICE</code> - faktura korekcyjna
                                </li>
                                <li>
                                    <code>SUPPLEMENTARY_INVOICE</code> - faktura uzupełniająca
                                </li>
                                <li>
                                    <code>RECEIPT</code> - paragon
                                </li>
                                <li>
                                    <code>INVOICE_FOR_RECEIPT</code> - faktura do paragonu
                                </li>
                                <li>
                                    <code>INVOICE_WITHOUT_VAT</code> - faktura bez VAT
                                </li>
                                <li>
                                    <code>PROFORMA_INVOICE_WITHOUT_VAT</code> - faktura proforma bez VAT
                                </li>
                            </ul>
                        </td>
                    </tr>
                    <tr>
                        <td>Typ dokumentu transportowego</td>
                        <td>
                            <ul>
                                <li>
                                    <code>WAYBILL</code> - list przewozowy
                                </li>
                                <li>
                                    <code>PROTOCOL</code> - protokół
                                </li>
                                <li>
                                    <code>PROFORMA_INVOICE</code> - faktura proforma
                                </li>
                                <li>
                                    <code>AUTHORIZATION</code> - upoważnienie
                                </li>
                                <li>
                                    <code>INSTRUCTION_FOR_CUSTOMS_DOCUMENTATION</code> - instrukcja do dokumentacji
                                    celnej
                                </li>
                                <li>
                                    <code>CUSTOMS_CLEARANCE_CARD</code> - karta odprawy celnej
                                </li>
                                <li>
                                    <code>EXPORTER_STATEMENT</code> - oświadczenie eksportera
                                </li>
                            </ul>
                        </td>
                    </tr>
                    </tbody>
                </table>

## 6. Paginacja w API
Wszystkie zasoby, w których występuje możliwość sterowania paginacją opierają się na poniższym schemacie.

### Request

<table class="table table-striped table-bordered">
                    <thead>
                    <tr>
                        <th>Pole</th>
                        <th>Opis</th>
                        <th>Wymagane</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>limit</td>
                        <td>Maksymalna liczba wyników dla zadanych filtrów, domyślnie 25, maksymalnie 100.</td>
                        <td>Nie</td>
                    </tr>
                    <tr>
                        <td>offset</td>
                        <td>Numer pozycji, od której zwracane będą wyniki, numerowany od 0, domyślnie 0.</td>
                        <td>Nie</td>
                    </tr>
                    <tr>
                        <td>filters []</td>
                        <td>Tablica filtrów. Filtry różnią się w zależności od endpointa.</td>
                        <td>Nie</td>
                    </tr>
                    </tbody>
                </table>

### Odpowiedź

<table class="table table-striped table-bordered">
                    <thead>
                    <tr>
                        <th>Pole</th>
                        <th>Opis</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>offset</td>
                        <td>Numer pozycji podany w parametrach żądania, lub domyślny, jeśli w parametrach nie podano
                            pozycji.
                        </td>
                    </tr>
                    <tr>
                        <td>limit</td>
                        <td>Maksymalna liczba wyników podana w parametrach żądania, lub domyślna, jeśli w parametrach
                            nie podano limitu.
                    </td></tr>
                    <tr>
                        <td>total</td>
                        <td>Całkowita liczba wyników dla zadanych filtrów.
                        </td>
                    </tr>
                    <tr>
                        <td>results []</td>
                        <td>Tablica wyników.
                        </td>
                    </tr>
                    </tbody>
                </table>
                
                
### Przykład paginacji
Jeśli chcemy wyświetlić masymalnie 10 pozycji na stronie, aby wyświetlić pierwszą stronę odpytujemy API ustawiając `offset` = 0 oraz `limit` = 10. Zwrotnie otrzymujemy informację, że wszystkich wyników total jest 126. Wiemy, że przy dziesięciu wynikach na stronie, mamy 13 stron wyników (ostatnia zawiera 6 pozycji). Aby wyświetlić drugą stronę odpytujemy API ustawiając `offset` = 10 oraz `limit` = 10.
## 7. Odpowiedzi API
API korzysta z następujących statusów odpowiedzi ([RFC 9110](https://www.rfc-editor.org/rfc/rfc9110)):

<table class="table table-striped table-bordered">
    <thead>
        <tr>
            <th>Status HTTP</th>
            <th>Opis</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>200 OK</td>
            <td>Poprawna odpowiedź z zawartością kolekcji lub obiektu.</td>
        </tr>
        <tr>
            <td>201 Created</td>
            <td>Poprawna odpowiedź - kod informuje o zmianach poczynionych na serwerze w postaci utworzenia nowego obiektu.</td>
        </tr>
                        <tr>
                            <td>202 Accepted</td>
                            <td>Poprawna odpowiedź - zapytanie zostało zaakceptowane, lecz jest jeszcze przetwarzane. W strukturze odpowiedzi znajduje się opis, jaki endpoint należy wywołać, aby uzyskać informacje o przetwarzanym elemencie.</td>
                        </tr>
                        <tr>
                            <td>204 No Content</td>
                            <td>Poprawna odpowiedź bez zawartości - kod informuje że serwer poprawnie przetworzył żądanie lecz odpowiedź nie wymaga zwrócenia dodatkowych informacji.</td>
                        </tr>
                        <tr>
                            <td>400 Bad Request</td>
                            <td>Błędne żądanie - zapytanie klienta zawiera niepoprawne dane.
                                Zwrócona odpowiedź zawiera strukturę komunikatów błędów w postaci informacji ogólnych oraz szczegółów niepoprawnie wypełnionych pól.
                                Na ich podstawie należy skorygować dane żądania i wysłać ponownie.
                            </td>
                        </tr>
                        <tr>
                            <td>401 Unauthorized</td>
                            <td>
                                Błąd autoryzacji - żądanie nie zawiera odpowiedniego tokenu do chronionego zasobu.
                                Należy taki uzyskać i spróbować ponowić żądanie.
                            </td>
                        </tr>
                        <tr>
                            <td>403 Forbidden</td>
                            <td>Odmowa dostępu do zasobu - przesłany token nie posiada odpowiednich uprawnień do chronionego zasobu.</td>
                        </tr>
                        <tr>
                            <td>404 Not Found</td>
                            <td>Nie znaleziono zasobu - żądanie klienta odnosi się do nieistniejącej ścieżki lub identyfikatora zasobu.</td>
                        </tr>
                        <tr>
                            <td>405 Method Not Allowed</td>
                            <td>
                                Niedozwolona metoda – metoda HTTP zawarta w żądaniu nie jest dozwolona dla wskazanego zasobu.
                                Odpowiedź zawiera również listę dozwolonych metod w nagłówku <code>Allow</code>.
                                Dozwolone metody zasobów możemy również odkryć przed ich użyciem.
                            </td>
                        </tr>
                        <tr>
                            <td>500 Internal Server Error</td>
                            <td>
                                Błąd wewnętrzny API - napotkano permanentny błąd uniemożliwiający zrealizowanie żądania.
                                Prosimy o zgłoszenie do działu technicznego pytań o status naprawy.
                            </td>
                        </tr>
                        <tr>
                            <td>503 Service Unavailable</td>
                            <td>API tymczasowo niedostępne - nie udało się zrealizować żądania, należy spróbować ponownie.</td>
                        </tr>
                        </tbody>
                    </table>
