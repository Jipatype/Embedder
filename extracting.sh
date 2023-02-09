#!/bin/sh
extractor="PATH/TO/EXTRACTOR"
font_input_folder="/PATH/TO/FONT_INPUT_FOLDER"
file_output_folder="PATH/TO/OUTPUT_FOLDER"
mkdir -p "$file_output_folder"
for file in "$font_input_folder/"*.otf; do
    file_name $(basename -a $file)
    "$extractor" -i "$file" -o "$file_output_folder/$file_name.txt"
done