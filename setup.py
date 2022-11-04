# please install python if it is not present in the system
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
 name='hello-world',
 version='1.0',
 packages=['hello-world'],
 license = 'MIT',
 description = 'hello world.',
 author = 'dev1145',
 author_email = '@gmail.com',
 keywords = ['hello-world','hello world'],
 long_description=long_description,
 long_description_content_type="text/markdown",
 url="https://github.com/dev1145/hello-world",
 install_requires=[ ],
 include_package_data=True,
)
