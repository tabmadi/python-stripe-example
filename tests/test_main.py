"""Tests for the Checkout Session request."""

from typing import TYPE_CHECKING

from config import Settings
from main import PRICE_IN_CENTS, create_checkout_session

if TYPE_CHECKING:
    import pytest


def test_session_request_uses_settings_and_integer_amount(monkeypatch: pytest.MonkeyPatch) -> None:
    """The request carries the configured URLs and an amount in cents."""
    sent: dict[str, object] = {}
    monkeypatch.setattr("stripe.checkout.Session.create", lambda **params: sent.update(params))

    settings = Settings(STRIPE_SECRET_KEY="sk_test_x", PAYMENT_SUCCESS_URL="https://shop/ok")
    create_checkout_session(settings)

    assert sent["success_url"] == "https://shop/ok"
    assert sent["mode"] == "payment"
    assert sent["line_items"] == [
        {
            "price_data": {
                "currency": "usd",
                "unit_amount": PRICE_IN_CENTS,
                "product_data": {"name": "Philosopher's Stone"},
            },
            "quantity": 1,
        },
    ]
