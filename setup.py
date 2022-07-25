from io import open
from setuptools import setup

version = '1.1'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()
setup(
    name = 'crypto_pay_api_sdk',
    author = 'Vyacheslav Zhigulin',
    author_email = 'muxellexum@gmail.com',
    url = 'https://github.com/althonos/crypto-pay-api-sdk',
    description = 'API for CryptoBot',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    license = 'MIT',
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages = ['crypto_pay_api_sdk'],
    where = ['where'],
    install_requires = ['requests'],
)