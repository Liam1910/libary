import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Calculating and PasswordGenerating Libary',
    version='1.0.0',
    author='Liam Schmallowsky',
    author_email='liamschmallowsky123@gmail.com',
    description='Can Calculate with Full and Decimal Numbers and can Generate Random 10 Character Long Passwords',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Liam1910/libary',
    license='MIT',
    packages=['libary'],
    install_requires=['requests'],
)
