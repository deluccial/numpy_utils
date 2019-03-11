import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

    name='numpy_utils',

    version='0.1',

    author="Luke DeLuccia",

    author_email="deluccial@gmail.com",

    description="Infix NumPy utilities.",

    long_description=long_description,

    long_description_content_type="text/markdown",

    py_modules=['numpy_utils'],

    packages=setuptools.find_packages(),

    install_requires=[

        'numpy',

    ],

    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

)
