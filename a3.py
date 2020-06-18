#
# Assignment 3
#
# Student Name : Aausuman Deep
# Student Number : 119220605
#
# Assignment Creation Date : February 15, 2020

import re

def open_nicholas():
    # this function returns the file pointer after opening nicholas.txt in read mode
    file = open("/Users/aausuman/Documents/College Stuff/Trimester 2/CS6507/Assignment_3/nicholas.txt", 'r')
    return file

def open_mary():
    # this function returns the file pointer after opening mary_roche.txt in read mode
    file = open("/Users/aausuman/Documents/College Stuff/Trimester 2/CS6507/Assignment_3/mary_roche.txt", 'r')
    return file

def spouses():
    # this function matches the marriage details in two files to identify possible spouses
    male_names, male_areas, male_years, male_quarters, male_volumes, male_pages = ([] for i in range(6))
    female_areas, female_years, female_quarters, female_volumes, female_pages = ([] for i in range(5))

    # defining the various regexps to identify our required data in the files
    name = re.compile(r"Marriage of(?P<name>\s+.+)")
    area = re.compile(r"Area(?P<area>\s+.+)")
    year = re.compile(r"Year(?P<year>\s+\d+)")
    quarter = re.compile(r"Quarter(?P<quarter>\s+\d+)")
    volume = re.compile(r"Volume No(?P<volume>\s+\d+)")
    page = re.compile(r"Page No(?P<page>\s+\d+)")

    # using above defined regexps to extract data and create lists of all the required parameters
    male = open_nicholas()
    for match in name.finditer(male.read()):
        male_names.append(str.strip(match.group('name')))
    male = open_nicholas()
    for match in area.finditer(male.read()):
        male_areas.append(str.strip(match.group('area')))
    male = open_nicholas()
    for match in year.finditer(male.read()):
        male_years.append(str.strip(match.group('year')))
    male = open_nicholas()
    for match in quarter.finditer(male.read()):
        male_quarters.append(str.strip(match.group('quarter')))
    male = open_nicholas()
    for match in volume.finditer(male.read()):
        male_volumes.append(str.strip(match.group('volume')))
    male = open_nicholas()
    for match in page.finditer(male.read()):
        male_pages.append(str.strip(match.group('page')))
    female = open_mary()
    for match in area.finditer(female.read()):
        female_areas.append(str.strip(match.group('area')))
    female = open_mary()
    for match in year.finditer(female.read()):
        female_years.append(str.strip(match.group('year')))
    female = open_mary()
    for match in quarter.finditer(female.read()):
        female_quarters.append(str.strip(match.group('quarter')))
    female = open_mary()
    for match in volume.finditer(female.read()):
        female_volumes.append(str.strip(match.group('volume')))
    female = open_mary()
    for match in page.finditer(female.read()):
        female_pages.append(str.strip(match.group('page')))

    # finally matching the essential parameters to identify the spouses
    for i in range(0, len(male_areas)):
        for j in range(0, len(female_areas)):
            if male_areas[i] == female_areas[j] \
                    and male_years[i] == female_years[j] \
                    and male_quarters[i] == female_quarters[j] \
                    and male_volumes[i] == female_volumes[j] \
                    and male_pages[i] == female_pages[j]:
                print("Possible match")
                print(male_names[j], "and MARY ROCHE in", male_areas[j], "in", male_years[j])
                print("Quarter =", male_quarters[j], ", Volume =", male_volumes[j], ", Page =", male_pages[j])

    return 0

