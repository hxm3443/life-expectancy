"""
File Name: utils.py
Description: This task involves writing tools for reading and processing the data, as well as defining data structures 
to store the data. The other tasks import and use these tools.
Author: Himani Munshi
Date: 12/10/2017
"""

#TASK 0

from rit_lib import *

Maindata = struct_type("Maindata", (str, 'country'), (list, 'values'))
Metadata = struct_type("Metadata", (str, 'region'), (str, 'income'))
CountryValue = struct_type("CountryValue", (str, 'country'), (float, 'value'))
Range = struct_type("Range", (str, 'country'), (int, 'year1'), (int, 'year2'), (float, 'value1'), (float, 'value2'))

def read_data(filename):
    """
    This function reads the data and metadata files and stores them in two dictionaries, one for each. The key for both
    the dictionaries is the country code and the value for one dictionary is an object of data structure Maindata
    and for the other is an object of data structure Metadata.
    parameter used: filename - a string, giving the partial name of the data file
    returns two dictionaries (data structures) representing the data contained in the main data and metadata files
    """

    path = "data/" + filename + "_data.txt"
    MainDct = {}    #code -> Maindata (key -> value)
    MetaDct = {}    #code -> Metadata (key -> value)

    #Building MainDct
    with open(path) as fd:
        fd.readline()   #ignores the header
        for line in fd:
            temp = line.strip().split(",")  #[country, code, values such as 50.1234 and so on]
            temp.pop()
            lst = [] #Building the second component of Maindata -> [(1960, 50.1234), (1961, 51.3555)...]
            year = 1960
            for elt in temp[2:]:
                if elt != "":
                    lst.append((year, float(elt)))
                else:
                    lst.append((year, 0)) #unavailable life expectancy
                year += 1
            MainDct[temp[1]] = Maindata(temp[0], lst)

    #Building MetaDct
    path = "data/" + filename + "_metadata.txt"
    with open(path) as fd:
        fd.readline()
        for line in fd:
            temp = line.strip().split(",")  #[country code, region, income]
            MetaDct[temp[0]] = Metadata(temp[1], temp[2])

    return MainDct, MetaDct

def filter_region(data, region):
    """
    This function filters data to only retain data for a specified region. Regardless of the specified region, this
    function always filters out the non-countries (larger groupings).
    parameters used: data - tuple containing two dictionaries MainDct and MetaDct
                     region - a string specifying a particular region by which to filter
    returns two dictionaries (data structures) representing data that has been filtered to only retain data corresponding
    to the specified region
    """

    f_MainDct = {}
    f_MetaDct = {}

    if region == "":
        return f_MainDct, f_MetaDct

    for key in data[1].keys():
        if region == "all":
            if data[1][key].region != "":
                f_MetaDct[key] = data[1][key]
                f_MainDct[key] = data[0][key]
        if region == data[1][key].region:
            f_MetaDct[key] = data[1][key]
            f_MainDct[key] = data[0][key]

    return f_MainDct, f_MetaDct

def filter_income(data, income):
    """
    This function filters data to only retain data for a specified income category. Regardless of the specified income
    category, this function always filters out the non-countries (larger groupings).
    parameters used: data - tuple containing two dictionaries MainDct and MetaDct
                     income - a string specifying a particular income category by which to filter
    returns two dictionaries (data structures) representing data that has been filtered to only retain data corresponding
    to the specified income category
    """
    f_MainDct = {}
    f_MetaDct = {}

    if income == "":
        return f_MainDct, f_MetaDct

    for key in data[1].keys():
        if income == "all":
            if data[1][key].income != "":
                f_MetaDct[key] = data[1][key]
                f_MainDct[key] = data[0][key]
        if income == data[1][key].income:
            f_MetaDct[key] = data[1][key]
            f_MainDct[key] = data[0][key]

    return f_MainDct, f_MetaDct

def main():
    """
    This function: 1. reads the data and metadata files
                   2. prints the total number of entities in the data file
                   3. prints the total number of countries in the data file
                   4. prints a summary of the different regions and the number of countries included in each region
                   5. prints a summary of the different income categories and the number of countries included in each
                      category
                   6. prompts the user to specify a region, and prints the names and country codes of all countries in
                      that region; if the user enters an invalid region, prints an appropriate message and continues
                      to the next requirement
                   7. prompts the user to specify an income category, and prints the names and country codes of all
                      countries in that income category; if the user enters an invalid income category, prints an
                      appropriate message and continues to the next requirement
                   8. enters a loop prompting the user for a country name or code
                      - if the user enters a valid country name or country code, prints out the life expectancy values
                        for that country
                      - if the user enters an invalid country name or country code, prints an appropriate message
                      - if the user hits enter to quit, exits the loop
    """

    data = read_data("worldbank_life_expectancy")
    MainDct = data[0]
    MetaDct = data[1]
    print("Total number of entities:", str(len(MainDct)))

    #counting the number of countries
    countryCount = 0
    for values in MetaDct.values():
        if values.region != "":
            countryCount += 1
    print("Number of countries/territories:", str(countryCount))

    print()

    print("Regions and their country count:")
    region_summary = {}  # key -> region, value -> CountryCount
    for value in MetaDct.values():
        if value.region != "":
            if value.region in region_summary:
                region_summary[value.region] += 1
            else:
                region_summary[value.region] = 1
    for key in region_summary.keys():
        print(key + ": " + str(region_summary[key]))

    print()

    print("Income categories and their country count:")
    income_summary = {}  # key -> income, value -> CountryCount
    for value in MetaDct.values():
        if value.region != "":
            if value.income in income_summary:
                income_summary[value.income] += 1
            else:
                income_summary[value.income] = 1
    for key in income_summary.keys():
        print(key + ": " + str(income_summary[key]))

    print()

    region = input("Enter region name: ")
    flag = False
    print_dct = {}
    for key in MetaDct.keys():
        if MetaDct[key].region == region:
            filtered_region = filter_region(data, region)
            print_dct[key] = filtered_region[0][key].country
            flag = True
    if flag == False:
        print("Region does not exist.")
    else:
        print("Countries in the '" + region + "' region: ")
        for key in print_dct.keys():
            print(print_dct[key], " (", key, ")", sep = "")

    print()

    income = input("Enter income category: ")
    print_dct_filter = {}
    flag = False
    for key in MetaDct.keys():
        if MetaDct[key].income == income:
            filtered_income = filter_income(data, income)
            print_dct_filter[key] = filtered_income[0][key].country
            flag = True
    if flag == False:
        print("Income category does not exist.")
    else:
        print("Countries in the '" + income + "' income category:")
        for key in print_dct_filter.keys():
            print(print_dct_filter[key], " (", key, ")", sep = "")

    print()

    flag = False
    user_input = input("Enter name of country or country code (Enter to quit): ")
    while user_input != "":
        for key in MainDct.keys():
            if user_input == key or user_input == MainDct[key].country:
                print("Data for " + user_input + ":")
                lst = MainDct[key].values
                flag = True
                for elt in lst:
                    if elt[1] != 0:
                        print("Year:", elt[0], "  Life expectancy:", elt[1])
        if flag == False:
            print("'" + user_input + "'" + "is not a valid country name or code")
        print()
        user_input = input("Enter name of country or country code (Enter to quit): ")

if __name__ == '__main__':
    main()

