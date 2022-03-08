import re

from setuptools import setup, find_packages

CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

with open("README.md", "r") as fh:
    long_description = fh.read()


def main():
    install_requires = [
        "attr==0.3.1",
        "certifi==2021.10.8",
        "charset-normalizer==2.0.12",
        "idna==3.3",
        "orjson==3.6.7",
        "pymarshaler==0.4.0",
        "python-dateutil==2.8.2",
        "requests==2.27.1",
        "six==1.16.0",
        "tqdm==4.63.0",
        "urllib3==1.26.8",
    ]
    with open('rumblesdk/version.py', encoding='utf-8') as config_py:
        version = re.search(r'^\s*__version__\s*=\s*[\"]([^\"]*)[\"]', config_py.read(), re.MULTILINE).group(1)
    setup(
        name="rumblesdk",
        version=version,
        author="n3integration",
        author_email="n3integration@gmail.com",
        description="Unofficial Rumble Network Discovery Python SDK",
        long_description=long_description,
        long_description_content_type="text/markdown",
        keywords='rumble sdk',
        url="https://github.com/n3integration/rumble-python-sdk",
        license='Apache Software License, Version 2.0, http://www.apache.org/licenses/LICENSE-2.0',
        packages=find_packages(exclude=['docs', 'test', 'test*', '*test', '*test*']),
        classifiers=CLASSIFIERS,
    )


if __name__ == "__main__":
    main()
