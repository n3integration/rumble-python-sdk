import os

from sys import version_info as py_version

from . import version


class API:
    """
    Configuration object containing the URLs for the Rumble API
    """
    RUMBLE_CONSOLE = os.getenv("RUMBLE_CONSOLE", "https://console.rumble.run")
    BASE_API_URL = f"{RUMBLE_CONSOLE}/api/v1.0"
    MAX_RETRY_ATTEMPTS = 5


class Client:
    """
    Configuration object containing the user agent string
    """
    VERSION = version.__version__
    USER_AGENT_STRING = f"rumble-python-sdk-{VERSION}"
    RUMBLE_UA_STRING = f"agent=rumble-python-sdk/{VERSION}; " \
                       f"env=python/{py_version.major}.{py_version.minor}.{py_version.micro}"


class Proxy:
    URL = None
    AUTH = None
