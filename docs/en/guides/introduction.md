---
title: Introduction
---

Previous version of documentation: https://api.globkurier.pl/v1/documentation

### 1. Getting Started
The GlobKurier API is based on REST architecture. Responses are returned in JSON format. Communication with the production endpoint is SSL-encrypted.

Environments are separated. To use the test API, you are required to have a production user account, provided at least one day has passed since registration or profile update (propagation time to the test environment). Test data is deleted at the end of the day.

You can send requests in JSON format with the Content-Type header set to application/json. In other cases, for POST requests, this header should be set to application/x-www-form-urlencoded.

To facilitate the integration and testing process, the documentation includes interactive requests.

Base URL:
```
https://api.globkurier.pl/v1
```
Test URL:
```
https://test.api.globkurier.pl/v1
```

### 2. Language Versions
The API language is selected by sending the accept-language header with an ISO 639-1 language code in the request.

Currently supported languages:
- pl
- en (default)

### 3. Resource Types
There are 3 resource types by authorization:

- no authorization required (e.g. fetching the country list)
- optional authorization (e.g. product search, which returns different products for guests and logged-in users) – marked in the documentation with a filter icon
- requiring authorization via token

### 4. Resource Discovery
You can retrieve available methods by querying any resource with the HTTP OPTIONS method. The response will include the following headers:

`Access-Control-Allow-Methods` – allowed HTTP methods for the resource, e.g., OPTIONS, GET
`Access-Control-Allow-Headers` – allowed headers for the resource, e.g., `x-auth-token`, `accept-language`, `x-currency`

This allows pre-verification whether a resource requires no token, or if your token provides sufficient access.

Attempting a not allowed method on a resource will result in the `405 Method Not Allowed error status`.

### 5. API Constants
The list contains constant values that must be provided in specific cases and cannot be retrieved from API resources.

<table class="table table-striped table-bordered">
<thead>
<tr>
<th>Name</th>
<th>Possible Values</th>
</tr>
</thead>
<tbody>
<tr>
<td>Dispatch Type</td>
<td>
<code>PICKUP</code>,
<code>POINT</code>,
<code>CROSSBORDER</code>
</td>
</tr>
<tr>
<td>Pickup Type</td>
<td>
<code>PICKUP</code>,
<code>POINT</code>,
<code>CROSSBORDER</code>
</td>
</tr>
<tr>
<td>Informational Labels</td>
<td>
<ul>
<li>
transport type: <code>GROUND</code>,
<code>AIR</code>
</li>
<li>
additional carrier information: <code>PACZKOMAT</code>,
<code>PACZKA_W_RUCHU</code>
</li>
</ul>
</td>
</tr>
<tr>
<td>Client Type</td>
<td>
<code>PERSON</code>,
<code>COMPANY</code>
</td>
</tr>
<tr>
<td>Shipment Purpose</td>
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
<td>Order Status</td>
<td>
<ul>
<li>
<code>NEW_SHIPMENT</code> – new
</li>
<li>
<code>IN_PROGRESS</code> – being processed by the system
</li>
<li>
<code>IN_TRANSIT</code> – in transit with the carrier
</li>
<li>
<code>DELIVERED</code> – delivered
</li>
<li>
<code>CANCELED</code> – canceled
</li>
<li>
<code>RETURNED_TO_SENDER</code> – returned to sender
</li>
</ul>
</td>
</tr>
<tr>
<td>Financial Document Type</td>
<td>
<ul>
<li>
<code>PROFORMA_INVOICE</code> – proforma invoice
</li>
<li>
<code>INVOICE</code> – VAT invoice
</li>
<li>
<code>CORRECTION_INVOICE</code> – corrective invoice
</li>
<li>
<code>SUPPLEMENTARY_INVOICE</code> – supplementary invoice
</li>
<li>
<code>RECEIPT</code> – receipt
</li>
<li>
<code>INVOICE_FOR_RECEIPT</code> – invoice for receipt
</li>
<li>
<code>INVOICE_WITHOUT_VAT</code> – invoice without VAT
                    </li>
                    <li>
                        <code>PROFORMA_INVOICE_WITHOUT_VAT</code> – proforma invoice without VAT
                    </li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>Transport Document Type</td>
            <td>
                <ul>
                    <li>
                        <code>WAYBILL</code> – waybill
                    </li>
                    <li>
                        <code>PROTOCOL</code> – protocol
                    </li>
                    <li>
                        <code>PROFORMA_INVOICE</code> – proforma invoice
                    </li>
                    <li>
                        <code>AUTHORIZATION</code> – authorization
                    </li>
                    <li>
                        <code>INSTRUCTION_FOR_CUSTOMS_DOCUMENTATION</code> – instruction for customs documentation
                    </li>
                    <li>
                        <code>CUSTOMS_CLEARANCE_CARD</code> – customs clearance card
                    </li>
                    <li>
                        <code>EXPORTER_STATEMENT</code> – exporter statement
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

### 6. API Pagination

All resources supporting pagination follow the scheme below.

#### Request

<table class="table table-striped table-bordered">
    <thead>
        <tr>
            <th>Field</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>limit</td>
            <td>Maximum number of results for given filters, default 25, maximum 100.</td>
            <td>No</td>
        </tr>
        <tr>
            <td>offset</td>
            <td>Index of the result from which results are returned, numbered from 0, default 0.</td>
            <td>No</td>
        </tr>
        <tr>
            <td>filters []</td>
            <td>Array of filters. Filters differ depending on the endpoint.</td>
            <td>No</td>
        </tr>
    </tbody>
</table>

#### Response

<table class="table table-striped table-bordered">
    <thead>
        <tr>
            <th>Field</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>offset</td>
            <td>The index provided in the request parameters or the default, if not specified.</td>
        </tr>
        <tr>
            <td>limit</td>
            <td>The maximum number of results provided in the request parameters or the default if not specified.</td>
        </tr>
        <tr>
            <td>total</td>
            <td>Total number of results for the given filters.</td>
        </tr>
        <tr>
            <td>results []</td>
            <td>Array of results.</td>
        </tr>
    </tbody>
</table>

#### Pagination Example

If you want to display a maximum of 10 records per page, to get the first page, query the API with `offset` = 0 and `limit` = 10. In response, you receive information that the total number of results is 126. You know that with ten results per page, there are 13 result pages (the last one has 6 results). To display the second page, query the API with `offset` = 10 and `limit` = 10.

### 7. API Responses

The API uses the following response statuses ([RFC 2616](https://www.ietf.org/rfc/rfc2616.txt)):

<table class="table table-striped table-bordered">
    <thead>
        <tr>
            <th>HTTP Status</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>200 OK</td>
            <td>Successful response with collection or object content.</td>
        </tr>
        <tr>
            <td>201 Created</td>
            <td>Successful response – indicates changes on the server in the form of a new object being created.</td>
        </tr>
        <tr>
            <td>202 Accepted</td>
            <td>Successful response – the request has been accepted but is still being processed. The response structure contains a description indicating which endpoint to call for information about the processed item.</td>
        </tr>
        <tr>
            <td>204 No Content</td>
            <td>Successful response with no content – indicates the server successfully processed the request but does not need to return any content.</td>
        </tr>
        <tr>
            <td>400 Bad Request</td>
            <td>Bad request – the client's request contains incorrect data. The returned response contains an error message structure with general information and details about incorrectly filled fields. Based on this, you should correct the request and resend.
            </td>
        </tr>
        <tr>
            <td>401 Unauthorized</td>
            <td>
                Authorization error – the request does not contain the appropriate token for the protected resource. You must obtain one and retry the request.
            </td>
        </tr>
        <tr>
            <td>403 Forbidden</td>
            <td>Access denied to the resource – the provided token does not have the required permissions for the protected resource.</td>
        </tr>
        <tr>
            <td>404 Not Found</td>
            <td>Resource not found – the client’s request refers to a non-existent path or resource identifier.</td>
        </tr>
        <tr>
            <td>405 Method Not Allowed</td>
            <td>
                Method not allowed – the HTTP method used in the request is not allowed for the specified resource. The response also includes a list of allowed methods in the <code>Allow</code> header. Allowed methods can be discovered before use.
            </td>
        </tr>
        <tr>
            <td>500 Internal Server Error</td>
            <td>
                Internal API error – a permanent error was encountered that prevents fulfilling the request. Please contact technical support for information about repair status.
            </td>
        </tr>
        <tr>
            <td>503 Service Unavailable</td>
            <td>API temporarily unavailable – the request could not be completed, please try again.</td>
        </tr>
    </tbody>
</table>
