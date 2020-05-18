import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="paxful-api-test",  # TODO remove test from name
    version="0.0.1",
    author="tholness",
    author_email="support.ec1818@tryninja.io",
    description="A python wrapper for Paxful REST API v1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tholness/Paxful-Python-API",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)