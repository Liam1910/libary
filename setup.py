import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='libary',
    version='0.1.0',
    author='Liam Schmallowsky',
    author_email='liamschmallowsky123@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Liam1910/libary',
    license='MIT',
    packages=['libary'],
    install_requires=['requests'],
)