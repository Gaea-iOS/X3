#!/bin/sh -l

echo $(which danger)

# Run danger
danger --dangerfile "./" ci