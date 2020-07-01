import csv
import re
import os
import shutil
import json
from pprint import pprint


def test():
    with open('photo.json') as f:
        my_dict = json.load(f)