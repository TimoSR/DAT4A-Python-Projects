import csv
import requests


# 2. Add a functionality so that the file can be called from cli with 2 arguments
# 2(a). path to csv file
# 2(b). an argument --file file_name that if given will write the content to file_name or otherwise will print it to
# the console.


def print_file_content(f_name):
    with requests.Session() as s:
        download = s.get(f_name)

        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')

        my_list = list(cr)

        for row in my_list:
            print(row)


def write_list_to_file(output_file, *strings):
    with open(output_file, 'w') as File:
        for s in strings:
            File.write(s + "\n")


def read_csv(input_file):
    with open(input_file, 'r') as File:
        l = []
        reader = csv.reader(File)
        for row in reader:
            l.append(row)
        return l
