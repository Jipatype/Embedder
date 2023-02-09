#!/bin/sh
cd "$(dirname "$0")"
extractor="/Users/anupap/MyFonttools/Font_emdedder/dist/extractor"
file_output_folder="PATH/TO/OUTPUT_FOLDER"
mkdir -p "$file_output_folder"
for file in *.otf; do 
    file_name $(basename -a $file)
    "$extractor" -i "$file" -o "$file_output_folder/$file_name.txt"
done