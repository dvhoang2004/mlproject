from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements from a file and returns them as a list.
    Removes any invalid or unnecessary entries like `-e .`.
    """
    requirements = []
    try:
        with open(file_path) as file:
            requirements = file.readlines()
            requirements = [req.strip() for req in requirements]  

            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)  
    except FileNotFoundError:
        print(f"Warning: {file_path} not found.")
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='HoangDV',
    author_email="dvh122004@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),  
)
