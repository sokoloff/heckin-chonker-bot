import os

from dotenv import load_dotenv

load_dotenv(dotenv_path=os.getenv("DOTENV_PATH"))


def getenv_boolean(var_name: str, default_value: bool = False):
    """Return the bool type from environment variable or default value.
    >>> os.environ["TEST_ENV_VAR"] = "true"
    >>> getenv_boolean("TEST_ENV_VAR")
    True
    >>> getenv_boolean("TEST_ENV_VAR_NOT_EXISTS")
    False
    >>> getenv_boolean("TEST_ENV_VAR_NOT_EXISTS", default_value=True)
    True
    """
    result = default_value
    env_value = os.getenv(var_name)
    if env_value is not None:
        result = env_value.upper() in ("TRUE", "1")
    return result


ENV = os.getenv("ENV", default="DEV").upper()

TELEGRAM_BOT_API_KEY = os.environ["TELEGRAM_BOT_API_KEY"]

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
OPENAI_API_URL = os.environ["OPENAI_API_URL"]
