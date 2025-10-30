from setuptools import setup,find_packages
from typing import List

HYPER_E_DOT_ = '-e .'
def get_requirement(filepath:str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPER_E_DOT_ in requirements:
            requirements.remove(HYPER_E_DOT_)

    return requirements        


setup(
    name="mlproject",
    version="0.0.1",
    author="vipin kumar",
    author_email="vipinmemon8123@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement("requirements.txt")


)