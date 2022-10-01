# Toolbox

Toolbox is a Python package that contains handy functions. 
It's main goal, however, is to demonstrate how to create a package.  
Check out [this](https://mikehuls.medium.com/create-your-custom-python-package-that-you-can-pip-install-from-your-git-repository-f90465867893)
article for a detailed explanation on how to create your 
custom Python package that is installable from your GitHub repo!

## Installation and updating
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Toolbox like below. 
Rerun this command to check for and install  updates .
```bash
pip install git+https://github.com/Liam1910/libary
```

## Usage
Features:
* Libary.Calculating.FullCalc() -> Takes input in the Console and calculates Full Numbers
* Libary.Calculating.DecimalCalc() -> Takes input in the Console and calculates Decimal Numbers (Example: 1.98)
* Libary.RandomPasswordGenerating.Generator() -> Generates an Random Password
* Libary.help() -> Displays Text in the Console for some help


#### Demo of some of the features:
```python
import Libary

libary.Calculating.FullCalc()

libary.Calculating.DecimalCalc()

libary.RandomPasswordGenerating.Generator()

libary.help()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
