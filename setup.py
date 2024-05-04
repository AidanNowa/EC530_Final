from setuptools import setup, find_packages

setup(
    name='boolean_solver_gui',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'sympy',
        'quine_mccluskey'  # Add other dependencies as needed
    ],
    entry_points={
        'console_scripts': [
            'boolean_solver_gui = boolean_solver_gui.main:main_function'
        ]
    },
    author='Aidan Nowakowski',
    author_email='aidannow@bu.edu',
    description='A simple boolean algebra solver with gui',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AidanNowa/EC530_Final',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
