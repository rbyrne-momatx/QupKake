"""Predict micro-pKa of organic molecules"""

# Add imports here
from ._version import get_versions
from .qupkake import *

__version__ = get_versions()["version"]

import os
import subprocess

# Fall back to user-specified or bundled xTB path
XTB_LOCATION = os.environ.get("XTBPATH")
if not os.path.exists(XTB_LOCATION):
    raise RuntimeError(
        f'xTB executable not found at: "{XTB_LOCATION}".\n'
        'Please set the "XTBPATH" environment variable or ensure xtb is built in the expected location.'
    )
