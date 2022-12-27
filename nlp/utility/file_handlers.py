

###
### Author : Mettu Venkata Ramireddy (venkata-ramireddy-mettu)
### Created Date : 27-Dec-2022
###

import json

def load_json(file_path):
    with open(file=file_path, mode="r") as jsf:
        return json.load(jsf)