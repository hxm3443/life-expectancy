"""
File Name: factors.py
Description: This task involves looking at how region and income affect life expectancy. Turtle graphics is used to 
generate plots to visualize the data. 
Author: Himani Munshi
Date: 12/10/2017
"""

#TASK 4

from utils import *
import turtle

def median_life_expectancy_income_or_region(filtered_data_income_or_region):
    """
    This function takes a filtered data set and computes the median life expectancy among the countries present for each
    year.
    parameter used: filtered_data_income_or_region - filtered data set containing two dictionaries
    returns a list containing median values of all countries per year from 1960 to 2015 based on region or income category
    """

    lst_year = []
    year = 1960
    medians_per_year = []
    while year <= 2015:
        for key in filtered_data_income_or_region[0].keys():
            if filtered_data_income_or_region[1][key].region != "" and filtered_data_income_or_region[0][key].values[year - 1960][1] != 0:
                lst_year.append(filtered_data_income_or_region[0][key].values[year - 1960][1])
        lst_year.sort()
        list_size = len(lst_year)
        if (list_size % 2 == 0):
            #even
            higher_value = lst_year[list_size//2]
            lower_value = lst_year[(list_size//2) - 1]
            median = (lower_value + higher_value)/2
            medians_per_year.append(median)
        else:
            medians_per_year.append(lst_year[(list_size - 1)//2])
        lst_year = []
        year += 1
    return medians_per_year

def plot_axes():
    """
    This function uses turtle to plot the x- and y- axes.
    pre-condition: turtle is at the origin facing East
    post-condition: turtle is at the origin facing East
    """

    turtle.setworldcoordinates(-10, -10, 60, 100)
    turtle.up()
    turtle.setpos(0, 0)
    turtle.down()
    turtle.forward(55)
    turtle.forward(-55)
    turtle.left(90)
    turtle.forward(90)
    turtle.forward(-90)
    turtle.right(90)

def plot_x_values():
    """
    This function uses turtle to plot the values on the x - axis.
    """

    #plotting values for x-axis
    turtle.right(90)
    turtle.up()
    turtle.forward(3)
    turtle.down()
    #insert value
    turtle.write("1960", False)
    turtle.up()
    turtle.setpos(0,0)
    turtle.down()
    turtle.left(90)
    turtle.up()
    turtle.forward(55)
    turtle.right(90)
    turtle.forward(3)
    turtle.down()
    #insert value
    turtle.write("2015", False)
    turtle.up()
    turtle.setpos(0, 0)
    turtle.down()
    turtle.left(90)

def plot_y_values():
    """
    This function uses turtle to plot the values on the y - axis.
    """

    turtle.right(180)
    turtle.up()
    turtle.forward(2)
    turtle.down()
    turtle.write(0, False)
    turtle.up()
    turtle.setpos(0,0)
    turtle.right(180)
    turtle.down()
    turtle.left(90)
    turtle.up()
    turtle.setpos(0, 10)
    turtle.down()
    turtle.left(90)
    turtle.up()
    turtle.forward(2)
    turtle.down()
    turtle.write(10, False)
    turtle.up()
    turtle.setpos(0,20)
    turtle.down()
    turtle.up()
    turtle.forward(2)
    turtle.down()
    turtle.write(20, False)
    turtle.up()
    turtle.setpos(0, 30)
    turtle.down()
    turtle.up()
    turtle.forward(2)
    turtle.down()
    turtle.write(30, False)
    turtle.up()
    turtle.setpos(0, 40)
    turtle.down()
    turtle.up()
    turtle.forward(2)
    turtle.down()
    turtle.write(40, False)
    turtle.up()
    turtle.setpos(0, 50)
    turtle.down()
    turtle.up()
    turtle.forward(2)
    turtle.down()
    turtle.write(50, False)
    turtle.up()
    turtle.setpos(0, 60)
    turtle.down()
    turtle.up()
    turtle.forward(2)
    turtle.down()
    turtle.write(60, False)
    turtle.up()
    turtle.setpos(0, 70)
    turtle.down()
    turtle.up()
    turtle.forward(2)
    turtle.down()
    turtle.write(70, False)
    turtle.up()
    turtle.setpos(0, 80)
    turtle.down()
    turtle.up()
    turtle.forward(2)
    turtle.down()
    turtle.write(80, False)
    turtle.up()
    turtle.setpos(0, 90)
    turtle.down()
    turtle.up()
    turtle.forward(2)
    turtle.down()
    turtle.write(90, False)
    turtle.up()
    turtle.setpos(0,0)
    turtle.down()
    turtle.right(180)

def label_y_axis():
    """
    This function labels the y - axis (it represents Life Expectancy).
    """

    turtle.up()
    turtle.setpos(0, 45)
    turtle.down()
    turtle.right(180)
    turtle.up()
    turtle.forward(7)
    turtle.down()
    turtle.write("Life Exp.", False)
    turtle.up()
    turtle.setpos(0, 0)
    turtle.down()
    turtle.right(180)

def label_x_axis():
    """
    This function labels the x - axis (it represents Year).
    """

    turtle.up()
    turtle.setpos(27.5, 0)
    turtle.right(90)
    turtle.forward(7)
    turtle.down()
    turtle.write("Year", False)
    turtle.up()
    turtle.setpos(0, 0)
    turtle.down()
    turtle.left(90)

def plotting_function(lst):
    """
    This function generates a line plot for the given list of median values based on region or income category
    parameter used: lst - a list containing median values of all countries per year from 1960 to 2015 based on region or
                          income category
    """

    x = 0
    turtle.up()
    while x <= 55:
        turtle.up()
        for elt in lst:
            turtle.setpos(x, elt)
            turtle.down()
            x += 1

def main():
    """
    This function: 1. reads the data and metadata files
                   2. filters the data to retain all income categories
                   3. computes the median life expectancy for each year, for each income category
                   4. uses turtle graphics to generate a line plot to show how the median life expectancy has changed
                      from 1960 to 2015 for countries belonging to each income category
                   5. prompts the user to hit enter to continue
                   6. repeats this analysis and generates a plot for the different region classifications
                   7. leaves the window open until the user clicks to close the window
    """

    data = read_data("worldbank_life_expectancy")
    data = filter_region(data, "all")
    MainDct = data[0]
    MetaDct = data[1]

    filtered_data_low_income = filter_income(data, "Low income")
    filtered_data_upper_middle_income = filter_income(data, "Upper middle income")
    filtered_data_lower_middle_income = filter_income(data, "Lower middle income")
    filtered_data_high_income = filter_income(data, "High income")

    plot_axes()
    plot_x_values()
    plot_y_values()
    label_y_axis()
    label_x_axis()

    turtle.pensize(3)
    median_lst1 = median_life_expectancy_income_or_region(filtered_data_low_income)
    median_lst2 = median_life_expectancy_income_or_region(filtered_data_upper_middle_income)
    median_lst3 = median_life_expectancy_income_or_region(filtered_data_lower_middle_income)
    median_lst4 = median_life_expectancy_income_or_region(filtered_data_high_income)
    turtle.pencolor("blue")
    plotting_function(median_lst1)
    turtle.pencolor("red")
    plotting_function(median_lst2)
    turtle.pencolor("light green")
    plotting_function(median_lst3)
    turtle.pencolor("orange")
    plotting_function(median_lst4)

    user_input = input("Do you want to continue? (Press Enter to continue): ")
    if user_input == "":
        turtle.Screen().clear()
        filtered_data_region1 = filter_region(data, "Sub-Saharan Africa")
        filtered_data_region2 = filter_region(data, "South Asia")
        filtered_data_region3 = filter_region(data, "Europe & Central Asia")
        filtered_data_region4 = filter_region(data, "Latin America & Caribbean")
        filtered_data_region5 = filter_region(data, "Middle East & North Africa")
        filtered_data_region6 = filter_region(data, "East Asia & Pacific")
        filtered_data_region7 = filter_region(data, "North America")
        plot_axes()
        plot_x_values()
        plot_y_values()
        label_y_axis()
        label_x_axis()

        turtle.pensize(3)
        median_lst1 = median_life_expectancy_income_or_region(filtered_data_region1)
        median_lst2 = median_life_expectancy_income_or_region(filtered_data_region2)
        median_lst3 = median_life_expectancy_income_or_region(filtered_data_region3)
        median_lst4 = median_life_expectancy_income_or_region(filtered_data_region4)
        median_lst5 = median_life_expectancy_income_or_region(filtered_data_region5)
        median_lst6 = median_life_expectancy_income_or_region(filtered_data_region6)
        median_lst7 = median_life_expectancy_income_or_region(filtered_data_region7)

        turtle.pencolor("blue")
        plotting_function(median_lst1)
        turtle.pencolor("red")
        plotting_function(median_lst2)
        turtle.pencolor("light green")
        plotting_function(median_lst3)
        turtle.pencolor("orange")
        plotting_function(median_lst4)
        turtle.pencolor("black")
        plotting_function(median_lst5)
        turtle.pencolor("purple")
        plotting_function(median_lst6)
        turtle.pencolor("yellow")
        plotting_function(median_lst7)
        turtle.done()

if __name__ == '__main__':
    main()







