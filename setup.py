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
        'aiohttp==3.6.2',
        'azure-common==1.1.23',
        'azure-nspkg==3.0.2',
        'cryptography==3.2',
        'yarl==1.4.2',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
    ]
)
