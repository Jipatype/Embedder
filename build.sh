#!/bin/sh
pyinstaller ./srcs/embedder.py --onefile 
pyinstaller ./srcs/extractor.py --onefile