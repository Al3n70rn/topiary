# Copyright (c) 2016. Mount Sinai School of Medicine
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Configuration file for readthedocs.org
"""
import sys

try:
    from unittest.mock import MagicMock
except:
    from mock import Mock as MagicMock

# replace all dependencies with Mock objects
MOCK_MODULES = []


def get_package_name(line, delimiters=[" ", ">", "<", "="]):
    for delim in delimiters:
        line = line.partition(delim)[0]
    return line

for requirement_line in open("requirements.txt", "r"):
    # get everything up until a version constraint like >=, >, <, <=, ==
    package_name = get_package_name(requirement_line)
    if package_name:
        print("Adding mock module for '%s'" % package_name)
        MOCK_MODULES.append(package_name)

sys.modules.update((mod_name, MagicMock()) for mod_name in MOCK_MODULES)
