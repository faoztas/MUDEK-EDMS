# Standard Library
import getpass

# Local Django
from Mudek.settings.base import *


if getpass.getuser() in ['root']:
    from Mudek.settings.production import *
else:
    from Mudek.settings.staging import *
