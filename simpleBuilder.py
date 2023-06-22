#!/usr/bin/env python

import os
import sys
import time
import json


data_json = {
    "compiler": "gcc",
    "run": "false",
    "dist": "./bin"
}
file_name = "simple_builder.json"
file_path = os.path.join(os.getcwd(), file_name)

green_color = '\033[92m'
red_color = '\033[91m'


def notification(message, color):

    return print(color+message+color)


def init():

    return


def file_exists(file_path):
    if os.path.exists(file_path):
        return True
    return False


def make_file(file_name, data_json):
    file = open(file_name, "w")
    json.dump(data_json, file)
    file.close()


def get_json_file(file_name):
    data_file = ""
    with open(file_name) as file:
        data_file = json.load(file)
    return data_file


if len(sys.argv) < 2:
    notification("Erro: 0 argumento de 1", red_color)
    time.sleep(2)
    sys.exit(1)


def get_args(args):
    arg_list = []
    for i in range(1, len(args)):
        arg_list.append(args[i])
    return arg_list


args = get_args(sys.argv)

print(args)

if file_exists(file_path):
    file = get_json_file(file_name)
    print(file)
else:
    make_file(file_name, data_json)
    file = get_json_file(file_name)
    print(file)

if "3" in args:
    print("\n o elemento esta na lista")
else:
    print("\n não esta")
