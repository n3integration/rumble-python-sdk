from .version import __version__
from .exception import ApiException

import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())
