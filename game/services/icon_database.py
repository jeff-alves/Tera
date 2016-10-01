# import Image
import io
import os
from zipfile import ZipFile
from PIL import Image

class IconDatabase(dict):
    __instance = None

    def __new__(self, *args, **kwargs):  # Singleton
        if not IconDatabase.__instance:
            IconDatabase.__instance = dict.__new__(self, *args, **kwargs)
        return IconDatabase.__instance

    def __init__(self):
        with ZipFile('data/icons.zip') as f:
            for name_f in f.namelist():
                name, ext = name_f.rsplit('.', 1)
                if ext == 'png':
                    self.add(name, Image.open(io.BytesIO(f.read(name_f))))

        for f in os.listdir("data/class-icons/"):
            name, ext = f.rsplit('.', 1)
            if ext == 'png':
                self.add(name, Image.open("data/class-icons/" + f))

    def add(self, name, img):
        self[name] = img
