from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'#Redirects to setup.py
def get_requirements(file_path:str)->List[str]:#takes in the file name i.e(requirements.txt) and returns a list of strings.
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='Student Performance Project',
    version='0.0.1',
    author='Harsh Chaturvedi',
    author_email='harsh.chats04@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')#Reads the Requirements from requirements.txt
)