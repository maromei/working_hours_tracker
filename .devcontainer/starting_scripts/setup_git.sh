#!/bin/bash

# The git directory will be managed by the host system
# This will cause a warning in the docker file
# --> need to mark it as safe

git config --global --add safe.directory /workspaces/working_hours_tracker

git config --global user.email "maromei@proton.me"
git config --global user.name "maromei"
