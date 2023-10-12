#!/usr/bin/python3

import datetime
import json

class FileStorage:
    def __init__(self):
        __file_path = "file.json"
        __objects = {}


    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        pass
    def save(self):
        pass
    def reload(self):
        pass

