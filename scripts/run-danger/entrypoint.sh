#!/bin/sh -l

# Install danger cli on the machine
yarn global add danger --dev

# install needed dependencies

# Run danger
danger --dangerfile "./" ci