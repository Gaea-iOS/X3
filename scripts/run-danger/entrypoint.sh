#!/bin/sh -l

sudo npm cache clean -f
sudo npm install -g n
sudo n stable

# Install danger cli on the machine
yarn add danger --dev

# install needed dependencies
yarn

# Run danger
danger --dangerfile "./dangerfile.js" ci