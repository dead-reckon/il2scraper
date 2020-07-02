import re
import os
import shutil
import json

header = """---
layout: card
title: Optimal Turn Speed
---
<div class="card">
    <div class="card-header">
        <h3 class="card-title">P_NAME</h3>
    </div>
    <div class="card-body">
        <h4>Engine Settings</h4>
        <p></p>
        <h4>Temp Settings</h4>
        <p></p>
        <h4>Stall Limits</h4>
        <p></p>
    </div>
</div>
"""

class CreateHTML:
    def __init__ (self, filename):
        self.filename = filename
        self.dir = path = os.getcwd() + "/cards/"

    def pull_json(self):
        planes = {}
        with open(self.filename) as f:
            planes = json.load(f)
        return planes

    def create_page(self, plane):
        p_name = plane["name"]
        circus = plane["circus"]
        l_engine = plane["engine"]
        l_stall = plane["stall"]
        l_temp = plane["temp"]

        path = self.dir + p_name + ".html"
        
        if circus:
            pass
        else:
            with open(path,'w', encoding = 'utf-8') as f:
                f.write(header)

    def generate(self):
        planes = self.pull_json()

        self.create_page(planes[0])
        # for line in planes:
        #     create_page(line)

p = CreateHTML("photo.json")

p.generate()