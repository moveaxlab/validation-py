from setuptools import find_packages, setup

setup(
    name='validation-python',
    version='1.1.0',
    maintainer='Michelle Laurenti',
    maintainer_email='michelle.laurenti@chainside.net',
    packages=find_packages(),
    install_requires=[
        'python-dateutil==2.7.3',
        'phonenumbers==8.10'
    ],
    include_package_data=True,
)
