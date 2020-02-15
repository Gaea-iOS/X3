#!/bin/bash

# Xcode run script entry.

set -e

python_scripts=(
    "update-bundle-version.py"
    "remove-unuse-architectures.sh"
)

current_dir=$(cd "$(dirname "$0")"; pwd)

pushd $current_dir > /dev/null

for script in ${python_scripts[@]}
do 
    echo "++++++++++ Running script: $script ++++++++++"
    if [[ $script == *.py ]]; then
        python3 $script
    else 
        sh $script
    fi
    echo "---------- done!!! ----------"
done

popd > /dev/null