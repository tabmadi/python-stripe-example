# Python Stripe Example

A short Python script that creates a [Stripe Checkout](https://docs.stripe.com/payments/checkout) Session and prints the URL of its payment page. It shows the smallest working Stripe integration, with typed configuration from `pydantic-settings`.

## What it shows

Stripe Checkout is a payment page that Stripe hosts. Your server does not collect card details. It creates a **Checkout Session** with the items and the return URLs, then sends the buyer to the session's URL:

1. The server creates a session with the line items, a success URL, and a cancel URL.
2. The buyer pays on the Stripe page.
3. Stripe redirects the buyer to the success URL, or to the cancel URL.

The script does step 1 for one product at 100 USD. Stripe amounts are integers in the smallest currency unit, so the amount is `10000` cents.

## Run it

1. Install [mise](https://mise.jdx.dev/getting-started.html), and create a [Stripe account](https://dashboard.stripe.com/register).
2. Install the tools and dependencies, and set your test mode secret key in `.env`:

   ```bash
   git clone git@github.com:tabmadi/python-stripe-example.git
   cd python-stripe-example
   mise install
   mise run setup
   cp .env.example .env
   ```

3. Create a session, then open the logged URL to see the payment page:

   ```bash
   mise run run
   ```

In test mode, the card number `4242 4242 4242 4242` pays with any future date and any CVC.

| Variable | Description | Default |
| --- | --- | --- |
| `STRIPE_SECRET_KEY` | A Stripe secret key. Use a test mode key, which starts with `sk_test_`. It is required | none |
| `PAYMENT_SUCCESS_URL` | Where Stripe sends the buyer after a payment | `http://localhost:8000/success` |
| `PAYMENT_CANCEL_URL` | Where Stripe sends the buyer after a cancel | `http://localhost:8000/cancel` |

## How it works

| File | Holds |
| --- | --- |
| [`src/main.py`](src/main.py) | Builds the session request and logs the session URL |
| [`src/config.py`](src/config.py) | The settings, read from the environment and `.env` |
| [`tests/test_main.py`](tests/test_main.py) | Checks the request without calling Stripe |

## What is deliberately missing

- **A web server**: the success and cancel URLs point to pages that this example does not serve.
- **Webhooks**: a real shop confirms the payment from the `checkout.session.completed` webhook, not from the redirect. A buyer can close the tab before the redirect.
- **Products and prices in Stripe**: the price is inline in the request. A real catalog uses Price objects.
- **Idempotency keys**: a retry of the same request can create a second session.

## Tasks

| Task | Does |
| --- | --- |
| `mise run setup` | Installs the locked dependencies and the git hooks |
| `mise run run` | Creates a Checkout Session and logs its URL |
| `mise run lint` | Runs `lint:py`, `lint:md`, and `lint:secrets` |
| `mise run format` | Applies every formatter |
| `mise run test` | Runs the tests |
| `mise run check` | Runs `lint` and `test`. Run it before you finish a change |
| `mise run ci` | Runs exactly what CI runs. The `pre-push` hook runs it too |

## License

Apache License 2.0. See [LICENSE](LICENSE).
