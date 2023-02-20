import os
import json
def deletedir():
    os.chdir('Harry Potter')
    for dir in os.listdir():
        os.chdir(dir)
        for dirr in os.listdir():
            if not os.listdir(dirr):
                os.rmdir(dirr)
        os.chdir('../')
    os.chdir('../')


def imperius(file):
    with open(file, 'r') as f:
        data = f.read()
        awards_json = json.loads(data)
    for award in awards_json:
        for aw in award['results']:
            aw['type'] = 'Winner'
    with open(file, 'w') as jf:
        json.dump(awards_json, jf)