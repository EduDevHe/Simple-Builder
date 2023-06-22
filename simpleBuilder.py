#!/usr/bin/env python

import os
import sys
import time
import json
import re
import subprocess

data_json = {
    "lang": "c",
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
    os.system("clear")
    data_json["lang"] = input("Language:")
    time.sleep(1)
    os.system("clear")
    data_json["compiler"] = input("Compiler:")
    time.sleep(1)
    os.system("clear")
    data_json["dist"] = input("Dist:")
    time.sleep(1)
    os.system("clear")
    run = input("Run [y/n]:")
    if run == "y":
        data_json["run"] = "true"
    else:
        if run == "n":
            data_json["run"] = "false"
        else:
            notification("Erro", red_color)
            time.sleep(2)
            sys.exit(1)
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


def compiler(compiler_data):
    try:
        sub_process = subprocess.run(
            compiler_data, capture_output=True, text=True)
        sub_process.check_returncode()
        os.system("clear")
        print(sub_process.stdout)
    except subprocess.CalledProcessError as error:
        notification("Error:"+error.returncode+"\n", red_color)
        notification(error.stderr, red_color)
    except Exception as exeption:
        notification(exeption, red_color)


if file_exists(file_path) is not True:
    if args[0] == "init":
        init()
        make_file(file_name, data_json)

    else:
        notification("Erro: need to init", red_color)
        time.sleep(2)
        sys.exit(1)

get_extension_file = re.search(r"\.([^.]+)$", args[0]).group(1)

executable = re.match(r"(.+?)(\.[^.]*$|$)", args[0]).group(1)

data_json_file = get_json_file(file_name)


if len(sys.argv) < 2 and file_exists(
        os.path.join(os.getcwd(), args[0])) is not True:
    notification("Erro: file not found", red_color)
    time.sleep(2)
    sys.exit(1)
else:
    if get_extension_file != data_json_file["lang"]:
        notification("Erro: file not found", red_color)
        time.sleep(2)
        sys.exit(1)
    else:
        if get_extension_file == data_json_file["lang"]:
            sorce_code = ""
            with open(args[0], "r") as file:
                sorce_code = file.read()
            compiler_comand = [data_json_file["compiler"],
                               "-o", executable, sorce_code]
            compiler(compiler_comand)
