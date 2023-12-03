#!/bin/bash
set -e
git clone https://github.com/TylerMS887/prune
echo "Installing..."
set +e
python prune/install.py
rm -rf prune
