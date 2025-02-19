from setuptools import find_packages, setup
from typing import List

JUNK="-e ."
def get_requirements(file_path:str)->List[str]:
    """ This function will return the list of requirements"""
    requirements=[
    ]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]
        if JUNK in requirements:
            requirements.remove(JUNK)
        return requirements

setup(
    name='ML-Project',
    version= '0.0.1',
    author= 'Aravind',
    author_email='gantaaravind1196@gmail.com',
    packages= find_packages(),
    install_requires=get_requirements('requirements.txt')
)