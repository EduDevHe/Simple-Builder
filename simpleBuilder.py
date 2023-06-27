#!/usr/bin/env python

import os
import sys
import time
import json
import re
import subprocess
import argparse

json_file_name = "simple_builder.json"
json_file_path = os.path.join(os.getcwd(), json_file_name)

colors = {
    "red": "\033[91m",
    "green": "\033[92m"
}


def notification(message, color):

    return print(color+message+color)


def init_config_file():
    os.system("clear")
    time.sleep(1)
    data_json = {
        "lang": "c",
        "compiler": "gcc",
        "run": "false",
        "dist": "./bin"
    }
    return data_json


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


def file_in_this_directory(file):
    return os.path.join(os.getcwd(), file)


def get_extension_file(file):

    return re.search(r"\.([^.]+)$", file).group(1)


def compiler_source(compiler_data):
    try:
        sub_process = subprocess.run(
            compiler_data, capture_output=True, text=True)
        sub_process.check_returncode()
        os.system("clear")
        print(sub_process.stdout)
    except subprocess.CalledProcessError as error:
        notification("Error: " + str(error.returncode) + "\n", colors["red"])
        print(error.stderr)
    except Exception as exception:
        print(exception)


def get_executable(file):
    return re.match(r"(.+?)(\.[^.]*$|$)", file).group(1)


def init():
    config_file = init_config_file()
    make_file(json_file_name, config_file)


def compiler(file):
    compiler_comand = [get_json_file(json_file_name)["compiler"],
                       "-o", get_executable(file), file]
    compiler_source(compiler_comand)


parser = argparse.ArgumentParser(description="Simple Builder")
parser.add_argument("-i", "--init", action="store_true",
                    help="Initialize Simple Builder")
parser.add_argument("-f", "--file", help="Compile a file selected")

args = parser.parse_args()
init_compiler = False
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

if args.init:
    try:
        init()
        init_compiler = True
        sys.exit(1)

    except Exception as error:
        print("Initialization error")
        init_compiler = False
        sys.exit(1)


if args.file and file_exists(json_file_name) is not True:
    parser.parse_args(args.init)
    sys.exit(1)
else:
    if args.file and get_extension_file(args.file) != get_json_file(json_file_name)["lang"]:
        print("Incompatible file type")
        sys.exit(1)
    else:
        compiler(args.file)
