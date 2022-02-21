import os

env = os.getenv('ENV', '')
if env:
    from .config_product import config
else:
    from .config_product import config
