# configuration file for readthedocs.org
import sys

try:
    from unittest.mock import MagicMock
except:
    from mock import Mock as MagicMock

# replace all dependencies with Mock objects
MOCK_MODULES = []
with open("requirements.txt", "r") as requirements_file:
    for requirement_line in requirements_file:
        parts = requirement_line.splt(" ")
        if parts:
            package_name = parts[0]
            MOCK_MODULES.append(package_name)

sys.modules.update((mod_name, MagicMock()) for mod_name in MOCK_MODULES)
