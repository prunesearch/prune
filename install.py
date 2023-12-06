#!/usr/bin/env python3 -x
import os
import sys
import shutil
import subprocess
version  = "1.0"

# Root
def prompt_sudo():
    ret = 0
    if os.geteuid() != 0:
        msg = "password for %u:"
        ret = subprocess.check_call("sudo -v -p '%s'" % msg, shell=True)
    return ret

if prompt_sudo() != 0:
    print("Unauthorized!")
    exit(5)

# Custom functions
def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")
def wait_key():
    ''' Wait for a key press on the console and return it. '''
    result = None
    if os.name == 'nt':
        import msvcrt
        result = msvcrt.getwch()
    else:
        import termios
        fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)

        try:
            result = sys.stdin.read(1)
        except IOError:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return result

# Introduction
print(f"Prune {version} Installation")
print()
print("This script will install Prune and the PSpider to your system.")
print("Before you continue, keep these disclaimers in mind:")
print("* Prune is currently in development. Don't use it in production.")
print("* Installing Prune is not a one-step process. You need to create")
print("  an SQLite database, set up the PSpider, and more.")
print("Press any key to continue...")
wait_key()

# New user
if os.name != "nt":
        print("This script will create a new unix user for prune. It will have")
        print("access to /etc/prune and other directories prune uses. You cannot")
        print("log into this user.")
        print("Press any key to create the prune user...")
        wait_key()
        os.system("useradd -u 7878 -r -M prune")

# Configuration
print("Prune can show built-in HTML-based tools such as a calculator, color picker,")
print("etc when related searches are queried. E.g. one can search a hex code to bring up")
print("the color picker for that hex code. Or one can type 'pi' to show the calculator")
print("with the value of pi.")
if query_yes_no("Do you want to enable this?"):
  html_miniresults = True
