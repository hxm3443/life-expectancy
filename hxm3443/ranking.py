"""
File Name: ranking.py
Description: This task involves processing the data and rank ordering it for a given year.
Author: Himani Munshi
Date: 12/10/2017
"""

#TASK 1

from utils import *

def compare(data):
    """
    This function is used to create and return a key for the .sort() function. The key forms the basis for sorting.
    """
    return data.value

def sorted_ranking_data(data, year):
    """
    This function ranks countries by their life expectancy for a particular year.
    parameters used: data - tuple containing two dictionaries MainDct and MetaDct
                     year - an integer representing the year under consideration
    returns a list of CountryValue structures, sorted in descending order
    """

    lst = []
    for key in data[0].keys():
        if data[1][key].region != "":
            country = data[0][key].country
            life_expectancy = float(data[0][key].values[year-1960][1])
            if life_expectancy != 0:
                lst.append(CountryValue(country, life_expectancy))
    lst.sort(key = compare, reverse = True)
    return lst

def main():
    """
    This function: 1. reads the data and metadata files
                   2. enters a loop that prompts the user for a year, followed by a region, followed by an income category
                      - if the year entered is -1, the program terminates
                      - otherwise, if any of the inputs is invalid or out of range, the loop restarts
                   3. for given valid inputs, the data is filtered to retain only the specified region and income category
                   4. data for the specified year is extracted and sorted, and the top ten and bottom ten life expectancies
                      for the given year are printed
                   5. additional requests are processed until the user enters -1 for the year
    """

    data = read_data("worldbank_life_expectancy")
    MainDct = data[0]
    MetaDct = data[1]

    valid_regions = []
    for key in MetaDct.keys():
        valid_regions.append(MetaDct[key].region)

    flag = True
    while flag:
            year = int(input("Enter year of interest (-1 to quit): "))
            if year == -1:
                flag = False
                continue
            if year < 1960 or year > 2015:
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
                print ("Invalid income")
                continue
            print()
            filtered_data_by_region = filter_region(data, region)
            filtered_data_by_region_and_income = filter_income(filtered_data_by_region, income)
            sorted_data_for_year_desc = sorted_ranking_data(filtered_data_by_region_and_income, year)
            sorted_data_for_year_asc = sorted_data_for_year_desc[::-1]
            print("Top 10 Life Expectancy for " + str(year))
            count = 0
            for i in range(0, len(sorted_data_for_year_desc)):
                count += 1
                if count <= 10:
                    print(str(i+1) + ": " + sorted_data_for_year_desc[i].country + " " + str(sorted_data_for_year_desc[i].value))
            print()
            print("Bottom 10 Life Expectancy for " + str(year))
            count = 0
            for i in range(0, len(sorted_data_for_year_asc)):
                count += 1
                if count <= 10:
                    print(str(len(sorted_data_for_year_asc) - i) + ": " + sorted_data_for_year_asc[i].country + " " + str(sorted_data_for_year_asc[i].value))
            print()

if __name__ == '__main__':
    main()





