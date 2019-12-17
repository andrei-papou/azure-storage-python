import setuptools


with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='azure-storage-python',
    version='0.0.1',
    author='Andrei Papou',
    author_email='andrei.papou@itechart-group.com',
    description='Async Python client for Azure SDK',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/andrei-papou/azure-storage-python',
    packages=setuptools.find_packages(),
    install_requires=[
        'aiodns',
        'aiohttp',
        'asn1crypto',
        'async-timeout',
        'attrs',
        'azure-common',
        'azure-nspkg',
        'azure-storage-python',
        'cchardet',
        'cffi',
        'chardet',
        'cryptography',
        'idna',
        'idna-ssl',
        'multidict',
        'pycares',
        'pycparser',
        'python-dateutil',
        'PyYAML',
        'six',
        'urllib3',
        'vcrpy',
        'wrapt',
        'yarl',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
    ]
)
