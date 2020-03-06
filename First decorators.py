# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 21:28:50 2020

@author: Niv Lifshitz
"""

import time

from itertools import zip_longest
def execution_time(func):
    def call_func(*args,**kwargs):
        epoch_time = time.time()
        result = func(args,kwargs)  #the result of the function
        run_time = time.time() - epoch_time
        print(f"runtime:{run_time}")
        print(" -- end of decorator --")
        return result
    
    return call_func

    
def arguments_printer(func):
    def arguments_passed(*args,**kwargs):
        if args:
            print("positional arguments:")
        if not args : #empty list and dictionary
            print("No arguments passed")
            return None
        for arg in args:  #positional arguments
            print(arg)
        if  kwargs:
            print("keyword arguments:")
        for k,v in kwargs.items():  #keyword arguments
            print(f'{k}= {v}')
        res = func(args,kwargs)  #the result of the function
        print(" -- end of decorator --")
        return res
    return arguments_passed


def object_printer(func):
    def object_passed(*args,**kwargs):
        if not args:
            print("positional arguments:")
        for arg in args:  #positional arguments
            print(f"{str(arg)} is {type(arg)}")
        if not kwargs:
            print("keyword arguments:")
        for k,v in kwargs.items():  #keyword arguments
            print(f'{k}= {v} ={str(v)} is {type(v)}')
        res = func(args,kwargs)
        print(" -- end of decorator --")
        return res
    return object_passed


def only_positive_parameters(func):  # A decorator to make sure the parameters passed to the function are positive.
    def wrapper(*args,**kwargs):
        for arg,v in zip_longest(args,kwargs.values(),fillvalue= 1):  #for efficency
            if arg < 0 or v < 0:
                res = "A negative parameter has been passed to the function..."
                return res
            res = func(args)
        print(" -- end of decorator --")
        return res
    return wrapper

