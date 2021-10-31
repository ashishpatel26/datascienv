from setuptools import setup, find_packages
import codecs
import os

with open("README.md") as f:
    long_description = f.read()

VERSION = '0.1.2'
DESCRIPTION = 'Data Science package for setup data science environment in single line'

# Setting up
setup(
    name="datascienv",
    version=VERSION,
    author="ashishpatel26",
    author_email="ashishpatel.ce.2011@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'scipy', 'matplotlib', 'seaborn', 
                      'scikit-learn', 'statsmodels', 'pyforest', 'pycaret', 'Flask', 'fastapi',
                      'jupyter', 'xgboost', 'imbalanced-learn', 'bokeh', 'kat',
                      'Boruta', 'spyder', 'mlxtend', 'lightgbm', 'catboost',
                      'tensorflow-cpu==2.6.0', 'tensorflow-gpu==2.6.0'],
    keywords=['Datascienv', 'Data Science installation in single line', 'data science', 'datascience', 'datasci', 'datascience environment'],
    url='http://github.com/ashishpatel26/datascienv',
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    platforms=["any"],
    zip_safe=True,
)
