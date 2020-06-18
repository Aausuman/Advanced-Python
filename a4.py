#
# Assignment 4
#
# Student Name : Aausuman Deep
# Student Number : 119220605
#
# Assignment Creation Date : February 22, 2020

import docx
import pyexcel
import os.path

def analyze(docfile):
    # This function creates an excel file with word frequencies of the desired document file
    doc = docx.Document(docfile)
    my_dict = {}
    # iterating paragraph wise
    for paragraph in doc.paragraphs:
        # replacing all non alphanumeric characters with a space
        for i in range(len(paragraph.text)):
            if not paragraph.text[i].isalnum():
                paragraph.text = paragraph.text.replace(paragraph.text[i], " ")
        paragraph.text = paragraph.text.lower()
        words = paragraph.text.split()
        # creating a dictionary of words and their counts
        for i in range(len(words)):
            if words[i] not in my_dict.keys():
                my_dict[words[i]] = 1
            else:
                my_dict[words[i]] += 1
    count_words = sum(my_dict.values())
    # updating dictionary to have frequency of words (divided by total) instead of counts
    for i in my_dict:
        my_dict[i] = float(my_dict[i]/count_words)
    # deleting all key value pairs with frequency less than 0.001
    delete = [key for key in my_dict if my_dict[key] < 0.001]
    for key in delete:
        del my_dict[key]
    row = 1
    # writing the dictionary into the worksheet and saving the appropriately named excel file
    my_list = [[k, v] for k, v in my_dict.items()]
    file = os.path.split(docfile)[1]
    filename = file.split(".")[0] + "_word_stats.xlsx"
    pyexcel.save_as(array=my_list, dest_file_name=filename, dest_sheet_name='Word Frequency Stats')
    return 0
