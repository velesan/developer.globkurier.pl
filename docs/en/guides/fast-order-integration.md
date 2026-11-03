---
title: Fast order Integration
---

## 1. Description
The fastest way to choose the best offer and place an order is through the endpoint [Simplified order placement - new](../api/globkurier.md#/Orders/orderCreateBestPrice). 

It is a combination of several points from [Full Integration (EN)](full-integration.md) in one. Instead of asking about all the products and addons and then placing the order, the system will automatically find the best (cheapest) offer and take it into execution. 

The endpoint structure is similar to endpoints [Get products](../api/globkurier.md#/Products/productSearch), [Get order price](../api/globkurier.md#/Order%20Pricing/orderGetPrice) and [Create order](../api/globkurier.md#/Orders/orderCreate).

## 2. Structure
You can use the strategy description [Full Integration (EN)](full-integration.md) to build a query, and the key differences are:

- in the `shipment` section:
    - there is no `productId` (we do not indicate a specific product)
    - the `integrationName` appears - the code of the carrier we want to send the shipment with. The codes can be downloaded from the endpoint described here: [Get carrier data (EN)](get-carrier-data.md) e.g. DPD, DHL 
- in the `addons` section we provide categories of additional services (add-ons) that we are interested in ordering along with the shipment (list: [Addon categories (EN)](addon-categories.md)) 

    np.

    ```json
    "addons": {
            "INSURANCE": {
                "value": 100
            }}
    ```

## 3. Action
For the given parameters, the system will try to find the cheapest offer that meets all the requirements. If a pointId is provided in the senderAddress section, the system will look for an offer that is shipped from a point (not necessarily with a courier pickup option -> instead of DPD, the DPD Pickup option will be selected).

## 4. Operation control
In the URL, by providing the createFully and onlyPricing parameters, we decide on the type of algorithm to be used:

| Parameter | Action |
| --- | --- |
| onlyPricing = true | The system will return a response with calculated rates and information about assigned allowances (similarly to the endpoint [Get order price](../api/globkurier.md#/Order%20Pricing/orderGetPrice)) |
| createFully = true | The system will automatically create the order both in the Globkurier system and forward it to the carrier. Similarly to the endpoint [Create order](../api/globkurier.md#/Orders/orderCreate) |

## 5. Response errors
There are several possible system responses due to the error:

| Response | Explanation |
| --- | --- |
|  "fields": {"addons[RETURN_SHIPMENT][id]": "This value is not available"} | No such add-on can be found for the specified parameters. The specified add-on should be deleted |
| {"fields": {"collectionType": "No product was found for the specified collection type."}} | No product found for the given shipping type (you need to change either the courier or the shipping type) |
| {"fields": {"shipment[integrationName]": "This offer is not available for given carrier."}} | There are no offers for the selected courier, shipping type and delivery type |

## 6. Correct answer

- `onlyPricing = true`: `200` with the price of the matched offer.
- Order placed: `201` with `number` (order number), `hash` and `price`. With `createFully = true` the response also contains `trackingNumber`, `pdfContent` (label, base64), `identifiers`, `formatContent` (label in a format other than A4) and `returnPdfContent` (with the `RETURN_SHIPMENT` add-on).
- `206`: the order was placed, but the synchronous registration with the carrier failed; the body is the same as for `201` plus `error`.
- Without `createFully` the order is registered with the carrier asynchronously.
