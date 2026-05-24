from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """Return list of requirements from requirements.txt."""
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            for line in file:
                requirement = line.strip()
                # ignore empty lines and editable installs
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst


#if __name__ == '__main__':
#    print(get_requirements())

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='chinmay palshetkar',
    author_email='chinmaypalshetkar30@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)




    
