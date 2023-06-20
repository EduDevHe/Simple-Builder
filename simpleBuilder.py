#!/usr/bin/env python

import os
import sys
import time



if len(sys.argv) < 2:
    print("\033[31mErro: 0 argumentos de 1\033[0m")
    time.sleep(2) 
    sys.exit(1)
    


def get_args(args):
    arg_list = []
    for i in range(1,len(args)):
        arg_list.append(args[i])
    return arg_list

args = get_args(sys.argv)

print(args)
        
if "3" in args:
    print("\n o elemento esta na lista")
else: 
    print("\n não esta")











