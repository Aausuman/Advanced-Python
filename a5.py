#
# Assignment 5
#
# Student Name : Aausuman Deep
# Student Number : 119220605
#
# Assignment Creation Date : March 2, 2020

from email.parser import Parser
import re
import string
import os

def emails_from(suspects):
    # This function prints all the emails sent by the employees 'Kenneth Lay' and 'Jeff Skilling'
    
    user_choice = int(input("Whose emails' summary do you wish to see? \n 1. Kenneth Lay \n 2. Jeff Skilling \n"))
    
    # Assigning folder and 'FROM' emails on the basis of choice
    if user_choice == 1:
        current_emails_path = list(suspects.keys())[0]
        from_emails = list(suspects.values())[0]
    elif user_choice == 2:
        current_emails_path = list(suspects.keys())[1]
        from_emails = list(suspects.values())[1]

    count = 1
    
    # Walking through all the files (within all sub-folders) in the chosen folder
    for root, dirs, files in os.walk(current_emails_path):
        for file in files:
            if count > 30:
                break
            with open(os.path.join(root, file), 'r') as f:
                try:
                    text_in_file = f.read()
                    parser_object = Parser()
                    email_content = Parser.parsestr(parser_object, text_in_file)
                    if email_content['From'] in from_emails:
                        # Printing out required details if the sender email is one of 'FROM' emails
                        date_regexp = re.compile(r"\d+\s\D+\s\d+")
                        # printing date in a better format rather than the raw format in email
                        date = date_regexp.search(str(email_content['Date']))
                        print("[%s]" % date.group().translate(str.maketrans('', '', string.punctuation)), end=" ")
                        print("%s -> " % email_content['From'], end="")
                        # printing the 'TO' address, and only first 'TO' address in case of multiple recipients
                        to_list = email_content['To'].split(",")
                        print("%s" % to_list[0])
                        print("Subject: %s" % email_content['Subject'])
                        count += 1
                except:
                    # Handling exceptions
                    print("An error occurred in processing", os.path.join(root, file), ", so skipping this file")
