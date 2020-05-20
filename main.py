from iter_class import Countries
import json
from file_writer import writer
from iter_hash import do_hash

if __name__ == '__main__':
    with open('countries.json') as f:
        templates = json.load(f)
    writer(Countries(templates))
    for i in do_hash('result.txt'):
        print(i)
