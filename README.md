# Embedder
These tools is for use to embedding any file into the .otf/.ttf font file.
- "embedder" is for embedding any file into the font file.
- "extractor" is for extracting file in the font file that embedded by "embedder".


# The tools need to install.
- python https://www.python.org/ 
- fonttools
```sh
~$ pip install fonttools
```
- pyinstaller
```sh
~$ pip install pyinstaller
```

# How to build.
```sh
~$ pyinstaller ./srcs/embedder.py
~$ pyinstaller ./srcs/extractor.py
```
The code will compile to under "dist" folder.

# How to use.
To embedding any file into the font file
```sh
~$ ./dist/embedder -i "path/to/input.otf" -o "path/to/output.otf" -m "path/to/embedding.txt"
```
To extracting file in the font file that embedded by "embedder".
```sh
~$ ./dist/extractor -i "path/to/input.otf" -o "path/to/output.txt"
```