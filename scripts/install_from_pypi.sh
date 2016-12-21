#!/bin/sh

PIP=pip
PIP=pip3
sudo -H ${PIP} install --quiet --upgrade pyfakeuse
${PIP} show pyfakeuse | grep -e "^Version"
