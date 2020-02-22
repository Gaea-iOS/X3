#!/bin/sh -l

# Install danger cli on the machine
yarn add danger --dev

# Run danger
danger --dangerfile "./" ci