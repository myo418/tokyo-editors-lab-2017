import os
import yaml

def getData():
    with open(os.path.dirname(__file__)  + '/../conf/conf.yml', 'r') as ymlfile:
        return yaml.load(ymlfile)
