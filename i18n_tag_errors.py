"""Selects html files from the directory and checks them for tag mistakes"""
import os

directory = "E:\\QA_test\\python_test\\test-i18n"


def html_file_list():
    """Check the directory for html files and make list of them."""
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    return html_files


def tag_errors(html_file_list):
    """
       Checks the contents of html files for tag mistakes
       :param html_file_list
       :return: returns errors, files and string indexes
       """

    incorrect_tag_list = ['<h2>', '<button>', '<p>', '<h>']
    errors = []

    for file in html_file_list:
        with open(file, "r") as f:
            result = f.readlines()
        for index, line in enumerate(result):
            for tag in incorrect_tag_list:
                if tag in line:
                    result2 = f"Error! There is no i18n tag in file {file} line {index + 1}"
                    errors.append(result2)
    return errors


print(*tag_errors(html_file_list()), sep='\n')
