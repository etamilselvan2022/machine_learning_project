from setuptools import setup
from typing import List

PROJECT_NAME="Housing-predictor"
VERSION="0.0.1"
AUTHOR="TAMIL"
DESCRIPTION="This is a FSDS First ML Project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement mention in requirements.txt file
    return this function is going to return a list which contains a list of libraries mentioned in requirements.txt file
    """
    with open (REQUIREMENT_FILE_NAME) as f:
        return f.readlines()



setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()
)


