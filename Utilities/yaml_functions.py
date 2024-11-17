"""
yaml functions contains method to read data from the yaml file
"""


from yaml import load
from yaml.loader import SafeLoader


class YAML_Reader:


    def __init__(self, file_name):
        self.file = file_name


    def reader(self):
        with open(self.file) as file:
            data = load(file, Loader=SafeLoader)
            return data