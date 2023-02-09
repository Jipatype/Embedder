#!/bin/sh
embedder="/PATH/TO/EMBEDDER"
font_input_folder="/PATH/TO/FONT_INPUT_FOLDER"
file_embedding="/PATH/TO/FILE.txt"
font_output_folder="/PATH/TO/FONT_OUTPU_FOLDER"
mkdir -p "$font_output_folder"
for file in "$font_input_folder/"*.otf; do
    file_name=$(basename -a $file);
    "$embedder" -i "$file" -o "$font_output_folder/$file_name" -m "$file_embedding"
done