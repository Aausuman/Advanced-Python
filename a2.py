#
# Assignment 2
#
# Student Name : Aausuman Deep
# Student Number : 119220605
#
# Assignment Creation Date : February 10, 2020

import re

def moolah(s):
    # returns a list of every Euro amount (as a string) that is mentioned in the input
    amounts = []
    regexp = re.compile(r'EUR\s?\d+(\.\d+)?')
    for match in regexp.finditer(s):
        amounts.append(match.group())
    return amounts


def bleep(s):
    # returns a modified copy of the input in which all four-letter words are replaced by ****
    regexp = re.compile(r'(^|\b)\S{4}(\b|$)')
    s = regexp.sub("****", s)
    return s


def to_english(s):
    # returns a modified copy of the input in which all numbers appearing in the original are spelled out in English
    units = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    regexp = re.compile(r'\d+')
    numbers = []
    for match in re.finditer(regexp, s):
        number = match.group()
        if number not in numbers:
            numbers.append(number)
            number_in_text = " ("
            for i in range(len(number)):
                index = int(number[i])
                number_in_text += units[index]
                number_in_text += " "
            number_in_text = number_in_text.rstrip() + ")"
            s = re.sub(r'\b{}\b'.format(number), number + number_in_text, s)
    return s


def harvest_emails(s):
    # returns a list of the email addresses that occur within the input
    potential_emails = re.findall(r'\S+@\S+', s)
    emails = []
    for potential_email in potential_emails:
        parts = potential_email.split("@", 1)
        local_part = parts[0]
        domain = parts[1]
        if re.match(r'^[A-Za-z0-9_.]+$', local_part) and re.match(r'^[A-Za-z0-9-.]+$', domain):
            local_part_flag = 1
            domain_flag = 1
            if local_part[0] != '.' and local_part[len(local_part)-1] != '.':
                for i in range(1, len(local_part)):
                    if local_part[i] == '.':
                        if local_part[i-1] == '.':
                            local_part_flag = 0
            else:
                local_part_flag = 0
            if '.' not in domain:
                domain_flag = 0
            domain_labels = domain.split(".")
            if domain[0] != '.' and domain[len(domain) - 1] != '.':
                for label in domain_labels:
                    if label[0] == '-' or label[len(label)-1] == '-':
                        domain_flag = 0
            else:
                domain_flag = 0
            if local_part_flag == 1 and domain_flag == 1:
                emails.append(potential_email)
    emails = sorted(emails, key=lambda x: (x.rsplit('@', 1)[::-1], x))
    return emails
