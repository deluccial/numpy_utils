import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

    name='numpy_utils',

    version='0.1.5',

    author="Luke DeLuccia",

    author_email="deluccial@gmail.com",

    description="NumPy utilities.",

    long_description=long_description,

    long_description_content_type="text/markdown",

    py_modules=['numpy_utils'],

    packages=setuptools.find_packages(),

    url="https://github.com/deluccial/numpy_utils.git",

    install_requires=[

        'numpy',

    ],

    classifiers=[

        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

)
