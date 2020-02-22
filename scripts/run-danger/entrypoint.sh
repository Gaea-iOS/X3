#!/bin/sh -l

# Install danger cli on the machine
yarn add danger --dev

# install needed dependencies
yarn

# Run danger
danger --dangerfile "./dangerfile.js" ci