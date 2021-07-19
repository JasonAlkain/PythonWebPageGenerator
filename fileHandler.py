import time
import os
import hashlib


def writeData(fileName='', data='', openMode='a'):
    data = data  # 'Hello, world'
    with open(fileName, openMode) as f:
        data = f.write(data)
        f.close()


def openFile(fileName=''):
    data = ''
    if fileName != '':
        with open(fileName, 'r') as f:
            data = f.read()
            f.close()
    return data
