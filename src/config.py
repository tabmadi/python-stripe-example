"""The configuration, read from the environment and `.env`."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """The Stripe key and the URLs that Checkout returns to."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    stripe_secret_key: str = Field(alias="STRIPE_SECRET_KEY")
    payment_success_url: str = Field(default="http://localhost:8000/success", alias="PAYMENT_SUCCESS_URL")
    payment_cancel_url: str = Field(default="http://localhost:8000/cancel", alias="PAYMENT_CANCEL_URL")
