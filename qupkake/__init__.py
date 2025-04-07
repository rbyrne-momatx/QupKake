"""Predict micro-pKa of organic molecules"""

# Add imports here
from ._version import get_versions
from .qupkake import *

__version__ = get_versions()["version"]

import os
import subprocess

try:
    # Check if xTB is installed via conda
    check_package = subprocess.run(["conda", "list", "xtb"], stdout=subprocess.PIPE)
    check_package.check_returncode()

    xtb_installed = False
    xtb_version = None

    for line in check_package.stdout.decode("utf-8").splitlines():
        if line.startswith("xtb "):
            xtb_installed = True
            xtb_version = line.split()[1]
            break

    if not (xtb_installed and xtb_version == "6.4.1"):
        raise AssertionError

    # Conda-installed xTB is not supported
    raise RuntimeError(
        'Conda version of xTB is currently not supported.\n'
        'Please compile it from source and export the path manually to the "XTBPATH" environment variable.'
    )

except (subprocess.CalledProcessError, AssertionError):
    # Fall back to user-specified or bundled xTB path
    XTB_LOCATION = os.environ.get("XTBPATH") or os.path.join(
        os.path.dirname(__file__), "xtb-641/bin/xtb"
    )

    if not os.path.exists(XTB_LOCATION):
        raise RuntimeError(
            f'xTB executable not found at: "{XTB_LOCATION}".\n'
            'Please set the "XTBPATH" environment variable or ensure xtb is built in the expected location.'
        )
