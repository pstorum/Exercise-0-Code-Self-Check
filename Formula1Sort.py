# Course: CS361 - Software Engineering
# Author: Peter Storum
# Assignment: Exercise 0
# Description: Program that takes a file that contains Formula 1 Driver data and outputs data in alphabetical order
# and numerical order

def read_f1_drivers():
    """
    :returns a 2d list of data pulled from a given text file
    """
    driver_data = [[], [], [], []]
    with open('CS361 Exercise 0 2021 F1 Drivers.txt') as file:
        temp_driver_arr = 1
        while temp_driver_arr:
            temp_driver_arr = file.readline()
            if not temp_driver_arr:
                break
            driver_arr = temp_driver_arr.split(maxsplit=3)
            driver_data[0].append(driver_arr[0])
            driver_data[1].append(driver_arr[1])
            driver_data[2].append(int(driver_arr[2]))
            driver_data[3].append(driver_arr[3].strip('\n'))
    return driver_data


def output_drivers_alphabetical(data):
    """
    takes the given data and sorts the last names alphabetically. The sorted list is then used to print data from the
    given data, displaying the data in alphabetical order.
    """
    last_names = []
    for name in data[1]:
        last_names.append(name)
    last_names.sort()
    for name in last_names:
        pos = data[1].index(name)
        print(data[0][pos], data[1][pos], data[2][pos], data[3][pos])


def output_drivers_numerical(data):
    """
    takes the given data and sorts the driver numbers. The sorted list is then used to print data from the
    given data, displaying the data in numerical order.
    """
    numbers = []
    for num in data[2]:
        numbers.append(num)
    numbers.sort()
    for num in numbers:
        pos = data[2].index(num)
        print(data[0][pos], data[1][pos], data[2][pos], data[3][pos])


driver_data = read_f1_drivers()
print("2021 F1 Drivers", '\n', "===============\n")
print("Drivers by Alphabetical Last Name", "\n", "=============================", '\n')
output_drivers_alphabetical(driver_data)
print('\n\n'"Drivers sorted by their numbers", "\n", "=============================", '\n')
output_drivers_numerical(driver_data)
