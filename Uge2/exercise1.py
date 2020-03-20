import csv
import argparse
import os
import platform


def print_file_content(file):
    """1A. can print content of a csv file to the console"""
    with open(file) as file_object:
        for line in file_object:
            print(line)


def write_list_to_file(output_file, list):
    """1B. can take a list of tuple and write each element to a new line in file"""
    # 1Ba udskift list med *list i parameter liste for at håndtere strings i stedet for en liste
    if output_file != None:
        with open(output_file, "w") as output:
            for el in list:
                output.write(el + "\n")
    else:
        for line in list:
            print(line)


def append_string_to_file(output_file, string):
    # bliver brugt i Exercise 2
    if output_file != None:
        with open(output_file, "a") as output:
            output.write(string + "\n")


def read_csv(input_file):
    """1C. take a csv file and read each row into a list"""
    with open(input_file) as f:
        reader = csv.reader(f)
        list = []
        for row in reader:
            list.append(str(row))

        return list


if __name__ == '__main__':
    """2A&B. Add a functionality so that the file can be called from cli with 2 arguments"""
    parser = argparse.ArgumentParser(
        description='A program that will write the content from file to new file_name or otherwise will print it to the console. Example usage: python exercise1.py ./oldfile.csv --file newfile.csv')
    parser.add_argument('path', help='The path to file')
    parser.add_argument('--file',
                        help='file_name that if given will write the content to file_name')
    # 3 man kan ikke bruge --help da den brokker sig over den allerede er optaget
    parser.add_argument('--h',
                        help='Help text in header')

    args = parser.parse_args()
    file_input = args.path
    filename = basename = os.path.basename(file_input)
    write_list_to_file(args.file, read_csv(file_input))
