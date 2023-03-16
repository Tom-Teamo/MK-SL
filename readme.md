# MK-SL(MarkDown Search Locally)
This is a simple local search engine for titles of markdown files. You can search whether one string exists in paticular directory path and where it is. The program will recursively search all the markdown files under the paticular directory path. 
## Installation
clone is all.
## Usage
run the `main.py`, and it receives two parameters:
1. `-f` `--folder-path`
    Not Required. Search string under this path. You can also change the default path in `main.py` with the `MARKDOWN_FILES_DIR` varaiable.
2. `-s` `--string`
    Required. the string you want to search
### Example
```
python main.y -f "C:\\Users\\Bala\\OneDrive\\Notes\\" -s "English"
```
