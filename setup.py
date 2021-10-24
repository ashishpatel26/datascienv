from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.01'
DESCRIPTION = 'Data Science package for setup data science environment in single line'
LONG_DESCRIPTION = 'A package that allow you to build data science environment in single line of code and save your time. It is include one line import package pyforest so you can upload all environment in single line of code'

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
                      'scikit-learn', 'statsmodels', 'pyforest', 'pycaret', 
                      'jupyter', 'xgboost', 'imbalanced-learn', 'bokeh', 
                      'Boruta', 'spyder', 'mlxtend', 'lightgbm', 'catboost'],
    keywords=['pandas', 'numpy', 'scipy', 'matplotlib', 'seaborn', 'scikit-learn', 'statsmodels', 'pyforest', 'pycaret', 'jupyter', 'xgboost', 'imbalanced-learn', 'bokeh', 'Boruta', 'spyder', 'mlxtend', 'lightgbm', 'catboost', 'Data Science', 'Package',
              'Data science environment setup package', 'Package', 'datascienv'],
    url='http://github.com/ashishpatel26/datascienv',
    include_package_data=True,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    zip_safe=True,
)
