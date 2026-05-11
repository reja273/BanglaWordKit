from setuptools import setup, find_packages
import os

setup(
    name="BanglaWordKit",  
    version="0.1.2",
    packages=find_packages(),
    include_package_data=True,  
    package_data={
        "BanglaWordKit": ["data/*.json"],  
    },
    install_requires=[],  
    author="Rejaul Karim",
    description="A comprehensive Bangla NLP library for Bangla Word conversion",
    long_description=open('README.md', encoding='utf-8').read(), 
    long_description_content_type='text/markdown',
    url="https://github.com/reja273/BanglaWordKit",
    project_urls={
        "Bug Tracker": "https://github.com/reja273/BanglaWordKit/issues",
        "Source Code": "https://github.com/reja273/BanglaWordKit",
        "Documentation": "https://github.com/reja273/BanglaWordKit/blob/main/README.md",
    },
)