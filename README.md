# Details Extractor - Python

## Project Overview

This Python project leverages the power of NLTK (Natural Language Toolkit) to extract name, date of flight, and destination from human-readable text strings. It provides a flexible solution for various use cases where extracting such information from textual descriptions is necessary.

## Virtual Environment
- Create a virtual environment to manage all the dependencies
```shell
python -m venv .venv
```
- Activate the virtual environment
```shell
./venv/Scripts/activate
```

## Dependencies
- Install the requirements from requirements.txt
```shell
pip install -r requirements.txt
```
- Install nltk models
```shell
python nltk-install.py
```

- Install the spacy model
```shell
python -m spacy download en_core_web_md
```

## Start the API server
```shell
flask --app main run
```