# aptman

aptman is a higher-level interface that implements common
apt(Debian-based distro package manager) commands for pacman,
The Arch Linux package manager.

## Available commands

```
aptman install package_names...
aptman update
aptman upgrade
aptman autoremove
aptman autoclean
aptman clean
aptman download package_name
aptman show package_name
aptman remove package_names...
aptman search query
aptman list --installed
aptman list --upgradeable
```

Learn more about commands using aptman --help

## Installation
Python(please not Python 2) has to be installed to use aptman naturally because it is written in Python.\
If you haven't installed it, first install it:

```
$ sudo pacman -S python3
```

Then you are ready to add it in your path(You need curl BTW. You can also use wget or sth similar else):

```
$ sudo python3 -c $(curl https://raw.githubusercontent.com/electromeow/aptman/master/install.py)
```

## License

This project is licensed under MIT License.
