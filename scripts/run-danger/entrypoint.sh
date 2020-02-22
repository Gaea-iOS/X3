#!/bin/sh -l

# Install danger cli on the machine
yarn add danger --dev

yarn danger init

# Run danger
danger --dangerfile "./" ci