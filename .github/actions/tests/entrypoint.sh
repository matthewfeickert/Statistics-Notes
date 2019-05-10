#!/bin/bash

function print_and_run () {
    printf "\n# %s\n" "${1}"
    eval $( echo "$1")
}

print_and_run "which python"
print_and_run "which pip"
print_and_run "pip install --upgrade -q pip setuptools wheel"
print_and_run "pip list"

# Already there, but to make it clear to reader
print_and_run "cd ${GITHUB_WORKSPACE}"

print_and_run "python --version"
print_and_run "pip --version"
print_and_run "pip install --upgrade -q -r binder/requirements.txt"
print_and_run "pip list"

print_and_run "pytest"
