from setuptools import setup, find_packages
import os

setup(
    name="BanglaWordKit",  
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,  
    package_data={
        'bangla_nlp': ['data/*.json'],
    },
    install_requires=[],  
    author="Rejaul Karim",
    description="A comprehensive Bangla NLP library for Bangla Word conversion",
    long_description=open('README.md', encoding='utf-8').read(), 
    long_description_content_type='text/markdown',
)