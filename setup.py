# Copyright 2024 Scaleway
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
from setuptools import find_packages, setup

name = "cirq-scaleway"
description = "A Cirq package to simulate and connect to Scaleway Quantum as a Service"
long_description = io.open("README.rst", encoding="utf-8").read()
requirements = open("requirements.txt").readlines()
requirements = [r.strip() for r in requirements]
cirq_packages = ["cirq_scaleway"] + [
    "cirq_scaleway." + package for package in find_packages(where="cirq_scaleway")
]
requirements += [f"cirq-core==1.3.0"]

setup(
    name=name,
    version="0.1.2",
    url="http://github.com/scaleway/cirq-scaleway",
    author="The Scaleway Developers",
    author_email="community@scaleway.com",
    python_requires=(">=3.10.0"),
    install_requires=requirements,
    license="Apache 2",
    description=description,
    long_description=long_description,
    packages=cirq_packages,
    package_data={"cirq_scaleway": ["py.typed"], "cirq_scaleway.json_test_data": ["*"]},
)
