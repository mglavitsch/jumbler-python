import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jumblepkg-mglavitsch",
    version="0.0.1",
    author="Michael Glavitsch",
    author_email="michael.glavitsch@gmail.com",
    description="A python library for jumbling letters within words.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT License",
    url="https://github.com/mglavitsch/jumbler-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
