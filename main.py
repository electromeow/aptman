#!/usr/bin/python3

import sys
import os

args = sys.argv[1:]
if len(args) < 1:
    sys.stderr.write(
        "No command specified. Usage: aptman command [params...]\n")
    exit(1)
command = args[0].lower().strip()
flags = list(filter(lambda i: i.startswith("-"),
                    map(lambda j: j.strip(), args[1:])
                    )
             )
params = list(filter(lambda i: not i.startswith("-"),
                     map(lambda j: j.strip(), args[1:])
                     )
              )

if command == "install":
    if "--help" in flags:
        sys.stderr.write("Usage: aptman install package_names...\n")
        exit(0)
    if len(params) < 1:
        sys.stderr.write("Usage: aptman install package_names...\n\
Installs the packages using pacman.\n\
Uses pacman -S.\n")
        exit(1)
    os.system("pacman -S "+' '.join(params))

elif command == "update":
    if "--help" in flags:
        sys.stderr.write(
            "Usage: aptman update\nUpdates the package cache.\nUses pacman -Syy.\n")
        exit(0)
    os.system("pacman -Sy")

elif command == "upgrade":
    if "--help" in flags:
        sys.stderr.write(
            "Usage: aptman upgrade\nUpdates the package cache and upgrades the packages.\nUses pacman -Syu.\n")
        exit(0)
    os.system("pacman -Syu")

elif command == "autoremove":
    if "--help" in flags:
        sys.stderr.write("Usage: aptman autoremove\nRemoves the dependencies\
installed on the system which aren't needed.\n")
        exit(0)
    os.system("pacman -Qtdq | pacman -Rs -")

elif command == "autoclean":
    if "--help" in flags:
        sys.stderr.write("Usage: aptman autoclean\nDeletes the unnecessary cached \
packages and unused package database.\nUses pacman -Sc.\n")
        exit(0)
    os.system("pacman -Sc")

elif command == "clean":
    if "--help" in flags:
        sys.stderr.write("Usage: aptman clean\nDeletes the cache folder.\n\
Note: This is an aggressive command that is not recommended if you don't know what you actually do.\n\
Uses pacman -Scc\n")
        exit(0)
    os.system("pacman -Scc")

elif command == "download":
    if len(params) < 1:
        sys.stderr.write("Usage: aptman download package_name\n")
    if "--help" in flags:
        sys.stderr.write(
            "Usage: aptman download package_name\nDownloads the packages without installing them.\nUses pacman -Sw\n")
        exit(0)
    os.system("pacman -Sw "+' '+params[0])

elif command == "show":
    if len(params) < 1:
        sys.stderr.write("Usage: aptman show package_name\n")
    if "--help" in flags:
        sys.stderr.write(
            "Usage: aptman show package_name\nShows the information about a package in the repositories.\nUses pacman -Si.")
        exit(0)
    os.system("pacman -Si "+params[0])

elif command == "remove":
    if len(params) < 1:
        sys.stderr.write("Usage: aptman remove package_names...\n")
    if "--help" in flags:
        sys.stderr.write("Usage: aptman remove package_names...\nRemoves the packages given.\nUses pacman -Rs.\n")
        exit(0)
    os.system("pacman -Rs "+' '.join(params))

elif command == "search":
    if len(params) < 1:
        sys.stderr.write("Usage: aptman search query\n")
    if "--help" in flags:
        sys.stderr.write("Usage: aptman search package_names...\nSearches packages. Uses pacman -Ss.\n")
        exit(0)
    os.system("pacman -Ss "+' '.join(params))

elif command == "list":
    if "--help" in flags:
        sys.stderr.write("Usage: aptman list --installed | --upgradeable\n\
Lists the packages available from the repository.\n\
Shows only installed packages if --installed flag is supplied.\n\
Shows the packages ready to upgrade if --upgradeable flag is supplied.\n")
        exit(0)
    if "--installed" in flags:
        os.system("pacman -Q")
    elif "--upgradeable" in flags:
        os.system("pacman -Qu")
    else:
        sys.stderr.write("Sorry, I couldn't find an equivalent of this command in pacman.\n\
If there is, contribute and make me happy: https://github.com/electromeow/aptman\n")

elif command == "--help":
    sys.stderr.write("""
aptman is a higher-level interface that implements common apt(The Debian-based distro package manager) commands for pacman, the Arch Linux package manager.
Usage: aptman command [params...]
Available commands:
install, update, upgrade, autoremove, autoclean,
clean, download, show, remove, search, list
To learn about a command, use aptman command --help
""")
    exit(0)

else:
    sys.stderr.write("Unknown command! Use aptman --help to see the list of commands!\n")
