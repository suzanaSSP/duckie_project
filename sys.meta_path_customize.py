import sys

class CustomImporter:
    def find_module(self, fullname, path=None):
        if fullname == "GraphDataBase":
            print("Module found")
            return self
        else:
            print("module not found")
            return None
        
    def load_module(self,fullname):
        if fullname == "neo4j":
            module = sys.modules.setdefault(fullname)
            return module
sys.meta_path.append(CustomImporter())

custom = CustomImporter()

from neo4j import GraphDatabase

custom.find_module("GraphDataBase")