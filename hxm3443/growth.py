"""
File Name: growth.py
Description: This task has inputs of a starting year and an ending year, and involves computing and rank ordering the 
absolute growth in life expectancy over the time period.  
Author: Himani Munshi
Date: 12/10/2017
"""

#TASK 2

from utils import *

def compare(data):
    """
    This function is used to create and return a key for the .sort() function. The key forms the basis for sorting.
    """
    return data.value

def sorted_growth_data(data, year1, year2):
    """
    This function ranks countries by absolute growth in life expectancy over a specified range of years.
    parameters used: data - tuple containing two dictionaries MainDct and MetaDct
                     year1 - an integer representing the starting year under consideration
                     year2 - an integer representing the ending year under consideration
    returns a list of CountryValue structures, sorted in descending order
    """

    lst = []
    for key in data[0].keys():
        country = data[0][key].country
        life_expectancy1 = float(data[0][key].values[year1 - 1960][1])
        life_expectancy2 = float(data[0][key].values[year2 - 1960][1])
        growth = abs(life_expectancy1 - life_expectancy2)
        if growth > 0 and life_expectancy1 != 0 and life_expectancy2 != 0:
            lst.append(CountryValue(country, growth))
    lst.sort(key = compare, reverse = True)
    return lst

def main():
    """
    This function: 1. reads the data and metadata files
                   2. enters a loop that prompts the user for a starting year, followed by an ending year, followed by a
                      region, followed by an income category
                      - if either the starting or ending year entered is -1, the program terminates
                      - otherwise, if any of the inputs is invalid or out of range, the loop restarts
                   3. for given valid inputs, the data is filtered to retain only the specified region and income category
                   4. data for the specified years is extracted and the growth values sorted, and the top ten and bottom
                      ten life expectancy growth values over the given range of years are printed
                   5. additional requests are processed until the user enters -1 for the starting or ending year
    """

    data = read_data("worldbank_life_expectancy")
    MainDct = data[0]
    MetaDct = data[1]

    valid_regions = []
    for key in MetaDct.keys():
        valid_regions.append(MetaDct[key].region)

    flag = True
    while flag:
        year1 = int(input("Enter starting year of interest (-1 to quit): "))
        if year1 == -1:
            flag = False
            continue
        year2 = int(input("Enter ending year of interest (-1 to quit): "))
        if year2 == -1:
            flag = False
            continue
        if year1 < 1960 or year1 > 2015 or year2 < 1960 or year2 > 2015:
            print("Valid years are 1960-2015")
            print()
            continue
        region = input("Enter region (type 'all' to consider all): ")
        if region not in valid_regions:
            print("'" + region + "'" + " is not a valid region")
            continue
        if region == "":
            print("Invalid region")
            continue
        income = input("Enter income category (type 'all' to consider all): ")
        if income == "":
            print("Invalid income")
            continue
        print()
        filtered_data_by_region = filter_region(data, region)
        filtered_data_by_region_and_income = filter_income(filtered_data_by_region, income)
        sorted_data_for_year_desc = sorted_growth_data(filtered_data_by_region_and_income, year1, year2)
        sorted_data_for_year_asc = sorted_data_for_year_desc[::-1]
        print("Top 10 Life Expectancy Growth: " + str(year1) + " to " + str(year2))
        count = 0
        for i in range(0, len(sorted_data_for_year_desc)):
            count += 1
            if count <= 10:
                print(str(i + 1) + ": " + sorted_data_for_year_desc[i].country + " " + str(
                    sorted_data_for_year_desc[i].value))
        print()
        print("Bottom 10 Life Expectancy Growth: " + str(year1) + " to " + str(year2))
        count = 0
        for i in range(0, len(sorted_data_for_year_asc)):
            count += 1
            if count <= 10:
                print(str(len(sorted_data_for_year_asc) - i) + ": " + sorted_data_for_year_asc[i].country + " " + str(
                    sorted_data_for_year_asc[i].value))
        print()


if __name__ == '__main__':
    main()

