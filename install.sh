#!/usr/bin/env bash

cp ./script.py ~/.git-walk.py
git config --global alias.walk '!python ~/.git-walk.py'
echo 'The extension has been successfully installed.'
