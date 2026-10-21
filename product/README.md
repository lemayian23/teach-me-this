# Product: a document-extraction API for Kenyan buyers

The thing this course builds toward. It is a real service, not a toy — the code
in `courses/` teaches, the code here earns.

**Working name:** TBD. Pick a domain once the endpoint actually returns JSON.

## The offer

Send a photo or PDF of a receipt, invoice, M-Pesa statement or SACCO sheet.
Get structured JSON back: amounts, dates, payee, line items, phone numbers.

Buyers are bookkeepers, SACCO treasurers, small shops reconciling statements —
people who today retype numbers into Excel by hand.

## Money model: metered credit packs

- Free tier: a monthly allowance, enough to evaluate, not enough to run on.
- Packs: buy N extractions with M-Pesa. Credits debit before the work runs,
  never after, so a failure cannot spend the customer's balance twice.
- No card required to try it. M-Pesa is the product, not a fallback.

Donations are not a business model here; they are a link on a lesson page.

## Rails

| Rail | Status | Why |
|------|--------|-----|
| Safaricom Daraja sandbox | Build here first | Free keys, M-Pesa Express simulator, no paperwork |
| Daraja production | Apply in parallel | Needs paybill/till number: business registration, bank, KRA docs |
| Paystack Kenya | Fallback / fastest first payment | STK Push without owning a till, ~1.5% domestic capped ~KES 2,000 |

Billing lives behind one module. Only `create_checkout()` and `handle_webhook()`
touch a provider, so swapping rails is a config change, not a rewrite.

## Endpoint contract

Mirrors what a good API product looks like: key in a header, work in the body,
one error shape, a header that tells the caller what the call cost.

```
POST /v1/extract
Authorization: Bearer sk_live_...
Content-Type: multipart/form-data        (the document)

200 OK
Content-Type: application/json
X-Credits-Used: 1
X-Request-Id: req_...

{ "fields": { "total": 1200.0, "currency": "KES", "date": "2026-10-19", "payee": "..." } }

402 Payment Required
{ "error": { "code": "insufficient_credits", "message": "...", "request_id": "req_..." } }
```

## Build order — this is the curriculum

| Course week | Product artifact |
|---|---|
| 1 | Extraction prompt that returns consistent text; f-string templates |
| 2 | Pydantic model for the response — bad output fails loudly, not silently |
| 3 | FastAPI route, Postgres tables for users, keys, credits ledger, Docker |
| 4 | Document chunking + retrieval when a page is too big for one prompt |
| 5 | Eval set of ~30 real documents; accuracy is measured before anyone pays |
| 6 | Deploy, `/healthz`, rate limits, error JSON above |
| 7 | Daraja sandbox STK Push + webhook that adds credits, pricing page, docs |

## Non-negotiable rules before money moves

1. Verify the webhook signature before crediting anyone. Always.
2. Idempotency: one M-Pesa `CheckoutRequestID` may credit the ledger exactly once.
3. Never log a full API key or phone number of a customer's document.
4. `.env` holds secrets and is git-ignored; nothing else works on a public repo.
