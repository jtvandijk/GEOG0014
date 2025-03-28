#! /bin/bash

# render
quarto render

# fix section numbers
python _section_numbers.py

# track changes
git add .
git commit -m "$1"

# publish
git push
