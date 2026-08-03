#! /usr/bin/bash

for i in *.ui; do
    echo "Converting $i to ${i%.*}.py"
    ~/Documents/catan-dice-tracker/venv/bin/pyside6-uic $i -o "${i%.*}.py"
done
echo "Completed all conversions."