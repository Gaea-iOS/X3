#!/bin/sh -l

npm cache clean -f
npm install -g n
n stable

# Install danger cli on the machine
yarn add danger --dev

# install needed dependencies
yarn

# Run danger
danger --dangerfile "./dangerfile.js" ci