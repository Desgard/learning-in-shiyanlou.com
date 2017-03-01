# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

class Document(object):
    def __init__(self, name):
        super(Document,self).__init__()
        self.name=name
        pass

    def Add(self, document):
        pass

    def GetChild(self):
        pass

    def Operation(self,depth):
        pass

    def Remove(self, document):
        pass

class File(Document):
    def __init__(self, name):
        super(File,self).__init__(name)
        pass

    def Add(self, document):
        pass

    def GetChild(self):
        pass

    def Operation(self,depth=1):
        print('-'*depth + self.name)
        pass

    def Remove(self, document):
        pass

class Folder(Document):
    m_Document= Document("None")

    def __init__(self, name):
        super(Folder,self).__init__(name)
        self.ls=list()
        pass

    def Add(self, document):
        self.ls.append(document)
        pass

    def GetChild(self):
        print(self.ls)
        pass

    def Operation(self,depth=1):
        print('-'*depth + self.name)
        for child in self.ls:
            child.Operation(depth+2)
            pass
        pass

    def Remove(self, document):
        pass

if __name__=="__main__":

    m_Document = Document("None")
    root = Folder("root")
    file1 = File("file1")
    root.Add(file1)
    folder1 = Folder("folder1")
    root.Add(folder1)
    folder2 = Folder("folder2")
    file2 = File("file2")
    folder2.Add(file2)
    folder3 = Folder("folder3")
    folder2.Add(folder3)
    folder1.Add(folder2)
    root.Operation(1)
