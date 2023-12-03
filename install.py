#!/usr/bin/env python3 -x
import os
import sys
import shutil
version  = "1.0"

# Custom functions
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
