__author__ = 'rui'


# -*-coding: utf-8 -*-
import os.path, time


class FileInfo:
    def __init__(self, name, fullName, fileSize, createTime):
        self.name = name
        self.fullName = fullName
        self.fileSize = fileSize
        self.createTime = createTime


class FileParsing:
    files = []

    def __init__(self):
        pass

    def getFiles(self):
        pass
