---
title: Introduction
---

Vorherige Version der Dokumentation: https://api.globkurier.pl/v1/documentation

## 1. Erste Schritte
Die GlobKurier API basiert auf der REST-Architektur. Antworten werden im JSON-Format zurückgegeben. Die Kommunikation mit dem Produktionsendpunkt ist SSL-verschlüsselt.

Die Umgebungen sind getrennt. Um die Test-API zu nutzen, benötigen Sie ein Benutzerkonto der Produktionsumgebung, wobei seit der Registrierung oder der Aktualisierung des Profils mindestens ein Tag vergangen sein muss (Propagierungszeit in die Testumgebung). Testdaten werden am Ende des Tages gelöscht.

Sie können Anfragen im JSON-Format senden, wobei der Header Content-Type auf application/json gesetzt ist. In anderen Fällen sollte dieser Header bei POST-Anfragen auf application/x-www-form-urlencoded gesetzt werden.

Um den Integrations- und Testprozess zu erleichtern, enthält die Dokumentation interaktive Anfragen.

Basis-URL:
```
https://api.globkurier.pl/v1
```
Test-URL:
```
https://test.api.globkurier.pl/v1
```

## 2. Sprachversionen
Die Sprache der API wird gewählt, indem in der Anfrage der Header accept-language mit einem ISO-639-1-Sprachcode gesendet wird.

Aktuell unterstützte Sprachen:

- pl
- en (Standard)

## 3. Ressourcentypen
Nach Autorisierung gibt es 3 Ressourcentypen:

- keine Autorisierung erforderlich (z. B. Abruf der Länderliste)
- optionale Autorisierung (z. B. Produktsuche, die für Gäste und angemeldete Benutzer unterschiedliche Produkte liefert) – in der Dokumentation mit einem Filtersymbol gekennzeichnet
- Autorisierung per Token erforderlich

## 4. Ressourcenerkennung
Sie können die verfügbaren Methoden abrufen, indem Sie eine beliebige Ressource mit der HTTP-Methode OPTIONS abfragen. Die Antwort enthält die folgenden Header:

- `Access-Control-Allow-Methods` – für die Ressource zulässige HTTP-Methoden, z. B. OPTIONS, GET
- `Access-Control-Allow-Headers` – für die Ressource zulässige Header, z. B. `x-auth-token`, `accept-language`, `x-currency`

Dadurch kann vorab geprüft werden, ob eine Ressource kein Token erfordert oder ob Ihr Token ausreichenden Zugriff bietet.

Der Versuch, eine nicht zulässige Methode auf einer Ressource auszuführen, führt zum `405 Method Not Allowed error status`.

## 5. API-Konstanten
Die Liste enthält konstante Werte, die in bestimmten Fällen angegeben werden müssen und nicht aus API-Ressourcen abgerufen werden können.

<table class="table table-striped table-bordered">
<thead>
<tr>
<th>Name</th>
<th>Mögliche Werte</th>
</tr>
</thead>
<tbody>
<tr>
<td>Versandart</td>
<td>
<code>PICKUP</code>,
<code>POINT</code>,
<code>CROSSBORDER</code>
</td>
</tr>
<tr>
<td>Abholart</td>
<td>
<code>PICKUP</code>,
<code>POINT</code>,
<code>CROSSBORDER</code>
</td>
</tr>
<tr>
<td>Informationslabels</td>
<td>
<ul>
<li>
Transportart: <code>GROUND</code>,
<code>AIR</code>
</li>
<li>
zusätzliche Carrier-Informationen: <code>PACZKOMAT</code>,
<code>PACZKA_W_RUCHU</code>
</li>
</ul>
</td>
</tr>
<tr>
<td>Kundentyp</td>
<td>
<code>PERSON</code>,
<code>COMPANY</code>
</td>
</tr>
<tr>
<td>Zweck der Sendung</td>
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
<td>Bestellstatus</td>
<td>
<ul>
<li>
<code>NEW_SHIPMENT</code> – neu
</li>
<li>
<code>IN_PROGRESS</code> – wird vom System bearbeitet
</li>
<li>
<code>IN_TRANSIT</code> – beim Carrier unterwegs
</li>
<li>
<code>DELIVERED</code> – zugestellt
</li>
<li>
<code>CANCELED</code> – storniert
</li>
<li>
<code>RETURNED_TO_SENDER</code> – an den Absender zurückgesendet
</li>
</ul>
</td>
</tr>
<tr>
<td>Typ des Finanzdokuments</td>
<td>
<ul>
<li>
<code>PROFORMA_INVOICE</code> – Proforma-Rechnung
</li>
<li>
<code>INVOICE</code> – MwSt.-Rechnung
</li>
<li>
<code>CORRECTION_INVOICE</code> – Korrekturrechnung
</li>
<li>
<code>SUPPLEMENTARY_INVOICE</code> – Ergänzungsrechnung
</li>
<li>
<code>RECEIPT</code> – Beleg
</li>
<li>
<code>INVOICE_FOR_RECEIPT</code> – Rechnung zum Beleg
</li>
<li>
<code>INVOICE_WITHOUT_VAT</code> – Rechnung ohne MwSt.
                    </li>
                    <li>
                        <code>PROFORMA_INVOICE_WITHOUT_VAT</code> – Proforma-Rechnung ohne MwSt.
                    </li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>Typ des Transportdokuments</td>
            <td>
                <ul>
                    <li>
                        <code>WAYBILL</code> – Frachtbrief
                    </li>
                    <li>
                        <code>PROTOCOL</code> – Protokoll
                    </li>
                    <li>
                        <code>PROFORMA_INVOICE</code> – Proforma-Rechnung
                    </li>
                    <li>
                        <code>AUTHORIZATION</code> – Vollmacht
                    </li>
                    <li>
                        <code>INSTRUCTION_FOR_CUSTOMS_DOCUMENTATION</code> – Anweisung für die Zolldokumentation
                    </li>
                    <li>
                        <code>CUSTOMS_CLEARANCE_CARD</code> – Zollabfertigungskarte
                    </li>
                    <li>
                        <code>EXPORTER_STATEMENT</code> – Ausführererklärung
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

## 6. API-Paginierung

Alle Ressourcen, die Paginierung unterstützen, folgen dem untenstehenden Schema.

### Anfrage

<table class="table table-striped table-bordered">
    <thead>
        <tr>
            <th>Feld</th>
            <th>Beschreibung</th>
            <th>Erforderlich</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>limit</td>
            <td>Maximale Anzahl der Ergebnisse für die gegebenen Filter, Standard 25, Maximum 100.</td>
            <td>Nein</td>
        </tr>
        <tr>
            <td>offset</td>
            <td>Index des Ergebnisses, ab dem Ergebnisse zurückgegeben werden, ab 0 nummeriert, Standard 0.</td>
            <td>Nein</td>
        </tr>
        <tr>
            <td>filters []</td>
            <td>Array von Filtern. Die Filter unterscheiden sich je nach Endpunkt.</td>
            <td>Nein</td>
        </tr>
    </tbody>
</table>

### Antwort

<table class="table table-striped table-bordered">
    <thead>
        <tr>
            <th>Feld</th>
            <th>Beschreibung</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>offset</td>
            <td>Der in den Anfrageparametern angegebene Index oder der Standardwert, falls nicht angegeben.</td>
        </tr>
        <tr>
            <td>limit</td>
            <td>Die in den Anfrageparametern angegebene maximale Anzahl der Ergebnisse oder der Standardwert, falls nicht angegeben.</td>
        </tr>
        <tr>
            <td>total</td>
            <td>Gesamtzahl der Ergebnisse für die gegebenen Filter.</td>
        </tr>
        <tr>
            <td>results []</td>
            <td>Array der Ergebnisse.</td>
        </tr>
    </tbody>
</table>

### Paginierungsbeispiel

Wenn Sie maximal 10 Datensätze pro Seite anzeigen möchten, fragen Sie für die erste Seite die API mit `offset` = 0 und `limit` = 10 ab. In der Antwort erhalten Sie die Information, dass die Gesamtzahl der Ergebnisse 126 beträgt. Sie wissen, dass es bei zehn Ergebnissen pro Seite 13 Ergebnisseiten gibt (die letzte hat 6 Ergebnisse). Um die zweite Seite anzuzeigen, fragen Sie die API mit `offset` = 10 und `limit` = 10 ab.

## 7. API-Antworten

Die API verwendet die folgenden Antwortstatus ([RFC 2616](https://www.ietf.org/rfc/rfc2616.txt)):

<table class="table table-striped table-bordered">
    <thead>
        <tr>
            <th>HTTP-Status</th>
            <th>Beschreibung</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>200 OK</td>
            <td>Erfolgreiche Antwort mit dem Inhalt einer Sammlung oder eines Objekts.</td>
        </tr>
        <tr>
            <td>201 Created</td>
            <td>Erfolgreiche Antwort – weist auf Änderungen auf dem Server in Form eines neu erstellten Objekts hin.</td>
        </tr>
        <tr>
            <td>202 Accepted</td>
            <td>Erfolgreiche Antwort – die Anfrage wurde angenommen, wird aber noch bearbeitet. Die Antwortstruktur enthält eine Beschreibung, welcher Endpunkt für Informationen über das bearbeitete Element aufzurufen ist.</td>
        </tr>
        <tr>
            <td>204 No Content</td>
            <td>Erfolgreiche Antwort ohne Inhalt – weist darauf hin, dass der Server die Anfrage erfolgreich verarbeitet hat, aber keinen Inhalt zurückgeben muss.</td>
        </tr>
        <tr>
            <td>400 Bad Request</td>
            <td>Fehlerhafte Anfrage – die Anfrage des Clients enthält falsche Daten. Die zurückgegebene Antwort enthält eine Fehlermeldungsstruktur mit allgemeinen Informationen und Details zu falsch ausgefüllten Feldern. Auf dieser Grundlage sollten Sie die Anfrage korrigieren und erneut senden.
            </td>
        </tr>
        <tr>
            <td>401 Unauthorized</td>
            <td>
                Autorisierungsfehler – die Anfrage enthält nicht das passende Token für die geschützte Ressource. Sie müssen eines beschaffen und die Anfrage wiederholen.
            </td>
        </tr>
        <tr>
            <td>403 Forbidden</td>
            <td>Zugriff auf die Ressource verweigert – das übergebene Token verfügt nicht über die erforderlichen Berechtigungen für die geschützte Ressource.</td>
        </tr>
        <tr>
            <td>404 Not Found</td>
            <td>Ressource nicht gefunden – die Anfrage des Clients bezieht sich auf einen nicht vorhandenen Pfad oder eine nicht vorhandene Ressourcenkennung.</td>
        </tr>
        <tr>
            <td>405 Method Not Allowed</td>
            <td>
                Methode nicht zulässig – die in der Anfrage verwendete HTTP-Methode ist für die angegebene Ressource nicht zulässig. Die Antwort enthält zudem eine Liste der zulässigen Methoden im Header <code>Allow</code>. Zulässige Methoden können vor der Verwendung ermittelt werden.
            </td>
        </tr>
        <tr>
            <td>500 Internal Server Error</td>
            <td>
                Interner API-Fehler – es ist ein dauerhafter Fehler aufgetreten, der die Erfüllung der Anfrage verhindert. Bitte wenden Sie sich an den technischen Support, um Informationen zum Stand der Behebung zu erhalten.
            </td>
        </tr>
        <tr>
            <td>503 Service Unavailable</td>
            <td>API vorübergehend nicht verfügbar – die Anfrage konnte nicht abgeschlossen werden, bitte versuchen Sie es erneut.</td>
        </tr>
    </tbody>
</table>
