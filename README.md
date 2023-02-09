# Embedder

These tools is for use to embedding any file into the .otf/.ttf font file.

- "embedder" is for embedding any file into the font file.
- "extractor" is for extracting file from the font file that embedded by "embedder".

# The tools need to install.

- python https://www.python.org/
- fonttools

```sh
$ pip install fonttools
```

- pyinstaller

```sh
$ pip install pyinstaller
```

# How to build.

```sh
$ pyinstaller ./srcs/embedder.py --onefile
$ pyinstaller ./srcs/extractor.py --onefile
```

The code will compile into under the "dist" folder.

# How to use.

To embedding any file into the font file

```sh
$ ./dist/embedder -i "path/to/input.otf" -o "path/to/output.otf" -m "path/to/embedding.txt"
```

If we want to embedding the file into multiple fonts file at once, shell script is the answer.

```sh
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
```

To extracting file in the font file that embedded by "embedder".

```sh
$ ./dist/extractor -i "path/to/input.otf" -o "path/to/output.txt"
```

If we want to extracting file from the font file that embedded by "embedder" at once , shell script is the answer.

```sh
#!/bin/sh
extractor="PATH/TO/EXTRACTOR"
font_input_folder="/PATH/TO/FONT_INPUT_FOLDER"
file_output_folder="PATH/TO/OUTPUT_FOLDER"
mkdir -p "$file_output_folder"
for file in "$font_input_folder/"*.otf; do
    file_name $(basename -a $file)
    "$extractor" -i "$file" -o "$file_output_folder/$file_name.txt"
done
```
