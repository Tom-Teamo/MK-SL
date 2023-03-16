import os

class ExtractTitle():
    def __init__(self, paths):
        self.paths = paths
        self.title = {}
    
    def extract(self):
        for path in self.paths:
            f = open(path, 'r', encoding='UTF-8')
            for line in f:
                if line.startswith("#"):
                    if path not in self.title.keys():
                        self.title[path] = []
                    self.title[path].append(line)
        return self.title