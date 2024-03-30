#!/bin/bash

# for some reason the first call always fails when building the environment
# --> redirect error and output to null. It will work fine once the ipykernel
# is installed.

hatch env create ipykernel
hatch run ipykernel:install
