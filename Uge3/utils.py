from os.path import isfile, join
import argparse
import exercise1
import os
import csv

def write_list_to_file(output_file, list):
    """can take a list of tuple and write each element to a new line in file"""
    if output_file != None:
        with open(output_file, "w") as output:
            for el in list:
                output.write(el + "\n")
    else:
        for line in list:
            print(line)