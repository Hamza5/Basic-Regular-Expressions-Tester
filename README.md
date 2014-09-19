![BRET](GUI/BRET-128.png)

## Basic Regular Expressions Tester

### Description
BRET is a Python3/PyQt4 application made in order to help writers of regular expressions to test their RegExps.

### Features
BRET has 3 modes of using the regular expressions :

* Find matches : Text will be searched to find every part that match the regular expression, each match will be displayed.
* Search and replace : Text will be returned replacing each part that match the regular expression by a given expression.
* Split text : Text will be fragmented on each part that matches the regular expression.

The text can be typed directly, loaded from a file, or downloaded from the web. The text file need to be encoded in UTF-8.

### Dependencies
In oreder to use BRET, both [Python 3](https://www.python.org/downloads/) and [PyQt4](http://www.riverbankcomputing.com/software/pyqt/download) must be installed on your system.

### Usage
BRET comes in 2 versions, command line version and GUI version.
The command line script can be found at `script/bret.py`. You can learn how to use it by typing in the terminal `script/bret.py --help`
The GUI program is `bret-pyqt.py`.

### License
The bret script is licensed under [GNU Lesser General Public License 3](http://www.gnu.org/licenses/lgpl-3.0.html) or any later version.

The GUI program is licensed under [GNU General Public License 3](http://www.gnu.org/licenses/gpl.html) or any later version.
