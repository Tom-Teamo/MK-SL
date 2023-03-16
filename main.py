import os
import argparse
from extractTitle import ExtractTitle

MARKDOWN_FILES_DIR = "C:\\Users\\cwwu\\OneDrive - USTC\\Notes\\"
FILE_LIST = []

parser = argparse.ArgumentParser(description='extract titles from local markdown files')
parser.add_argument('-f', '--folderPath', default=MARKDOWN_FILES_DIR, type=str, help="the root folder path where markdown files you wanna search lie")
parser.add_argument('-s', '--string', required=True, type=str, help="the string you wanna search for")

def searchDir(dirPaths):
    for dirPath in dirPaths:
        for root, dirs, files in os.walk(dirPath):
            for file in files:
                if file.endswith(".md"):
                    FILE_LIST.append(root + file)
            newDirPaths = [root + ele + "\\" for ele in dirs]
            if len(newDirPaths) != 0:
                searchDir(newDirPaths)
            else:
                break

def main():

    '''
    Simulate the args
    '''
    # argv = ["", "-s", "GPU", "-f", "C:\\Users\\cwwu\\OneDrive - USTC\\Notes\\D2L\\"]
    # args = parser.parse_args(argv[1:])

    '''
    parse args
    '''
    args = parser.parse_args()
    dirPath = args.folderPath
    strSearch = args.string

    #get all md files path, store in global variable FILE_LIST
    searchDir([dirPath])

    '''
    get all titles, store in directionary pathTitle
    key: path
    value: title
    '''
    titleClass = ExtractTitle(FILE_LIST)
    pathTitle = titleClass.extract()
    
    '''
    print results
    '''
    print("'" + strSearch + "'" + " in folowing files:")
    for key,values in pathTitle.items():
        for value in values:
            if strSearch in value:
                print("\t"+ key)
                break

if __name__ == "__main__":
    main()