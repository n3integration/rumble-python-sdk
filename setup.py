import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='rumble-python-sdk',
    version='2.10.0',
    author="n3integration",
    author_email="n3integration@gmail.com",
    description="An unofficial Python SDK for the Rumble Discovery Platform API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/n3integration/rumble-python-sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2.0 License",
        "Operating System :: OS Independent",
    ],
)