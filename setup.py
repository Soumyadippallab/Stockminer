from setuptools import setup, find_packages

setup(
    name="stockminer",
    version="0.1.0",
    description="A Python package for analyzing NSE stocks and market indices with TDA crash detection and random selection analysis.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Rajdeep Chaterjee, Soumyadip Das",
    author_email="cse.rajdeep@gmail.com, dassoumyadip204@gmail.com",
    url="https://github.com/Soumyadippallab/Stockminer.git",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "pandas>=2.0.0",
        "yfinance>=0.2.40",
        "yahooquery>=2.3.0",
        "tqdm>=4.66.4",
        "numpy>=1.26.0",
        "scikit-learn>=1.4.2",
        "scipy>=1.13.1",
        "matplotlib>=3.9.0",
        "seaborn>=0.13.2",
        "ripser>=0.6.4",
        "persim>=0.3.5",
        "openpyxl>=3.1.2",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
