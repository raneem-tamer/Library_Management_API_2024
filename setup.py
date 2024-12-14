from setuptools import setup, find_packages

setup(
    name='LibraryManagementAPI',  
    version='0.1.0',  # Initial version
    author='Raneem Tamer',  
    description='Library Management System API',
    packages=find_packages(),  
    install_requires=[  # List of dependencies
        'flask>=1.1',
        'sqlalchemy>=1.3',
        'pytest>=6.0',
        'flake8>=3.8',
        
    ],
    
)
