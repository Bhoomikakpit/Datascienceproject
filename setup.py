from setuptools import find_packages, setup
from typing import List

v1 = '-e .'
def get_requirement(file_path:str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirement = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace("\n","") for req in requirement]

        if v1 in requirement:
            requirement.remove(v1)
    return requirement


setup(
name = 'dsproject',
version = '0.0.1',
author = 'Bhoomi',
packages = find_packages(),
install_requires = get_requirement('requirement.txt')
)