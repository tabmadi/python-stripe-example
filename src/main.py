"""Create a Stripe Checkout Session for one product and log the payment page URL."""

import logging

import stripe

from config import Settings

logger = logging.getLogger(__name__)

# Stripe amounts are integers in the smallest currency unit: 10000 cents is 100 USD.
PRICE_IN_CENTS = 10000


def create_checkout_session(settings: Settings) -> stripe.checkout.Session:
    """Create a Checkout Session in payment mode for one Philosopher's Stone."""
    stripe.api_key = settings.stripe_secret_key

    return stripe.checkout.Session.create(
        mode="payment",
        customer_email="edward.elric@example.com",
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "unit_amount": PRICE_IN_CENTS,
                    "product_data": {"name": "Philosopher's Stone"},
                },
                "quantity": 1,
            },
        ],
        success_url=settings.payment_success_url,
        cancel_url=settings.payment_cancel_url,
        metadata={"order_id": "13435"},
    )


def main() -> None:
    """Create the session and log the URL of its payment page."""
    session = create_checkout_session(Settings())
    logger.info("Checkout Session %s: %s", session.id, session.url)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
