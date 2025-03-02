import os

import pkg_resources
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="whisperx",
    py_modules=["whisperx"],
    version="3.3.1",
    description="Time-Accurate Automatic Speech Recognition using Whisper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.9, <3.13",
    author="Max Bain",
    url="https://github.com/m-bain/whisperx",
    license="BSD-2-Clause",
    packages=find_packages(exclude=["tests*"]),
    entry_points={
        "console_scripts": ["whisperx=whisperx.transcribe:cli"],
    },
    include_package_data=True,
    extras_require={"dev": ["pytest"]},
)
