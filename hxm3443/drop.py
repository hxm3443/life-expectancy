"""
File Name: drop.py
Description: This task involves computing the largest drops in life expectancy experienced across any portion of the
entire timeline.
Author: Himani Munshi
Date: 12/10/2017
"""

#TASK 3

from utils import *

def compare(data):
   """
   This function is used to create and return a key for the .sort() function. The key forms the basis for sorting.
   """
   return data.value2 - data.value1

def sorted_drop_data(data):
   """
   This function identifies the 10 worst drops in life expectancy throughout the 1960-2015 timeframe.
   parameter used: data - tuple containing two dictionaries MainDct and MetaDct
   returns a sorted list of Range structures
   """

   max_drop_for_country = []
   for key in data[0].keys():
       if data[1][key].region != "" and isDataValid(data[0][key].values):
            life_expectancy_values = data[0][key].values
            drop_range_values = []
            drop_values = []
            for i in range (0, len(life_expectancy_values)):
                for j in range(i+1, len(life_expectancy_values)):
                    drop = life_expectancy_values[j][1] - life_expectancy_values[i][1]
                    if life_expectancy_values[j][1] != 0.0 and life_expectancy_values[i][1] != 0.0 and life_expectancy_values[i][0] < life_expectancy_values[j][0]:
                       drop_range_values.append(Range(data[0][key].country, life_expectancy_values[i][0], life_expectancy_values[j][0], float(life_expectancy_values[i][1]), float(life_expectancy_values[j][1])))
                       drop_values.append(drop)
            if (len(drop_values) == 0):
                continue

            max_drop_index = drop_values.index(min(drop_values))
            max_drop_for_country.append(drop_range_values[max_drop_index])
   max_drop_for_country.sort(key = compare)
   return max_drop_for_country

def main():
   """
   This function: 1. reads the data and metadata files
                  2. filters the data to retain all regions and income categories
                  3. data from the entire 1960 to 2015 timeframe is analyzed; the largest drop in life expectancy is
                     computed for each country; these values are sorted and the largest 10 drops are printed
   """

   data = read_data("worldbank_life_expectancy")
   MainDct = data[0]
   MetaDct = data[1]
   max_drop_for_country = sorted_drop_data(data)

   print("Worst life expectancy drops: 1960 to 2015")
   counter = 0
   for i in range(0, len(max_drop_for_country)):
       counter += 1
       if counter <= 10:
           print(str(counter) + ": " + max_drop_for_country[i].country + " from " + str(
               max_drop_for_country[i].year1) + "(" + str(max_drop_for_country[i].value1) + ")" + " to " + str(
               max_drop_for_country[i].year2) + "(" + str(max_drop_for_country[i].value2) + ")" + ": " + str(
               max_drop_for_country[i].value2 - max_drop_for_country[i].value1))

def isDataValid(values):
    """
    This function checks if the data is valid by checking that only countries that contain data for atleast two years are
    considered provided that data for life expectancy should not be zero when there are just two years.
    parameter used: values - list of tuples with each entry of the form (year, life expectancy)
    returns True or False
    """

    flag = False
    counter = 0
    for i in range(len(values)):
        if values[i][1] != 0:
            counter += 1
        if counter == 2:
            flag = True
            break
    if flag:
        return True
    return False

if __name__ == '__main__':
    main()

