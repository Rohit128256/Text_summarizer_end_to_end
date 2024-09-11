from setuptools import find_packages, setup
from typing import List

with open('README.md','r',encoding="utf-8") as f:
    long_desc = f.read()

HYPEN_E_DOT = '-e .'
def get_requirements (file_path : str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name = 'ml_project',
    version = '0.0.0',
    author = 'Rohit',
    author_email = 'rohitsaha128256@gmail.com',
    description = " a simple text summarizer app ",
    long_description = long_desc,
    url = "https://github.com/Rohit128256/Text_summarizer_end_to_end",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)