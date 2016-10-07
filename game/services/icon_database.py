import os
from zipfile import ZipFile
from wx.lib.embeddedimage import PyEmbeddedImage
from util.util import singleton

@singleton
class IconDatabase(dict):

    def __init__(self):
        dict.__init__(self)
        with ZipFile('data/icons.zip') as f:
            for name_f in f.namelist():
                name, ext = name_f.rsplit('.', 1)
                if ext == 'png':
                    self.add(name, PyEmbeddedImage(f.read(name_f), False))

        for f in os.listdir("data/class-icons/"):
            name, ext = f.rsplit('.', 1)
            if ext == 'png':
                with open("data/class-icons/" + f, 'rb') as file:
                    self.add(name, PyEmbeddedImage(file.read(), False))

        for f in os.listdir("res/"):
            name, ext = f.rsplit('.', 1)
            if ext == 'png' or ext == 'ico':
                with open("res/" + f, 'rb') as file:
                    self.add(name, PyEmbeddedImage(file.read(), False))

    def add(self, name, img):
        self[name] = img
