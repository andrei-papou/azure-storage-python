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
        'aiodns==2.0.0',
        'aiohttp==3.6.2',
        'asn1crypto==1.2.0',
        'async-timeout==3.0.1',
        'attrs==19.3.0',
        'azure-common==1.1.23',
        'azure-nspkg==3.0.2',
        'cchardet==2.1.5',
        'cffi==1.13.2',
        'chardet==3.0.4',
        'cryptography==2.8',
        'idna==2.8',
        'idna-ssl==1.1.0',
        'multidict==4.7.1',
        'pycares==3.1.0',
        'pycparser==2.19',
        'python-dateutil==2.8.1',
        'PyYAML==5.2',
        'six==1.13.0',
        'urllib3==1.24.3',
        'vcrpy==3.0.0',
        'wrapt==1.11.2',
        'yarl==1.4.2',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
    ]
)
