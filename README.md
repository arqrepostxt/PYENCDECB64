
PYENCDECB64 is a Pyton project of a tool to Encode/Decode text to base 64 with release for windows with executable exported to pyencdecB64/dist/pyencdecbase64/pyencdecbase64.exe.

# Software details
The tool features one mini window with 2 tabs. The first tab displays a Text box with a button that encodes the text to base 64 code. The second tab displays the same interface, but the button decodes the base 64 code from the Text box.<br>

# Requirements
The present project needs Python v3.5, PyQt5 and PyInstaller. You can read more details about each resource bellow.<br>  
Python v3.5 and supperior - To run a Python script code on a manchine is necessary Python already installed and this projects requires Python v3.5 to generate the software with visual interface using resources from PyQt5.
### How to install Python
To install the latest Python version follow the official link: [https://www.python.org/downloads/](https://www.python.org/downloads/) <br>

PyQt5 - Is a Python toolkit that provides sources for displaying an user friendly visual user interface for python script.<br>
### Here is how to install PyQT5
To install PyQT5 follow this single step guide copy and paste the bellow command on your terminal 
```
pip install PyQt5
```
<br>

Pyinstaller - Provides a solution to build python program for windows with .exe executable.<br>

### How to install Pyinstaller to create .exe from python script 
To install Pyinstaller follow this simple instruction to run the bellow command on your terminal 
```
pip install pyinstaller
```


# Guide Tutorial to build the exe binary for windows
After installed the requirements, run the bellow command on your terminal 'pyinstaller' 
```
pyinstaller -onefile  -windowed --pyencdecbase64.py
```

# Know issues
> - Copy/Paste may me denied when running the exe version in Windows when not started with 'Run as Adminstrator'.
> - The exe file size could become relatively exaggerated if the machine already have certain python libraries. There is a simple solution to reduce the file size of the .exe created with pyinstaller that consists in using the following command on your terminal to create the .exe file : 
```
pyinstaller --noconfirm --onedir --console  pyencodebase64.py
```