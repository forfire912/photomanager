#!/usr/bin/env python3
"""
Setup script for Photo Manager
"""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="photo-manager",
    version="1.0.0",
    author="forfire912",
    description="A CLI tool to manage photo/video collections with duplicate detection and date-based organization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/forfire912/photomanager",
    py_modules=["photo_manager"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Graphics",
        "Topic :: System :: Filesystems",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "photo-manager=photo_manager:main",
        ],
    },
    keywords="photo video duplicate organize exif management",
    project_urls={
        "Bug Reports": "https://github.com/forfire912/photomanager/issues",
        "Source": "https://github.com/forfire912/photomanager",
    },
)
