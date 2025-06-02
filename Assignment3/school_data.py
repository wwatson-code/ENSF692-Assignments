# school_data.py
# AUTHOR NAME: William Watson
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
import pandas as pd
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here
years_combined = np.array([year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022])
    
# 3D array containing [Years, School Name, and Grade]
global school_data_3D
school_data_3D = years_combined.reshape(10,20,3)


# You may add your own additional classes, functions, variables, etc.

def get_user_input(school_index_dict):
    user_input = input(" Enter School name or code here (e.g. 'Centennial High School' or '1224'): ")
    if user_input in school_index_dict.keys():
        return school_index_dict[user_input]
    else:
        raise ValueError("You must enter a valid school name or code")
    

def print_school_stats(key, dict):
    print("School Name: ")
    
    return



def main():
    print("")
    print("***** ENSF 692 School Enrollment Statistics *****")
    print("")
    # Print Stage 1 requirements here
    
    print("Shape of full data array: ",school_data_3D.shape)

    # Extract unique lists of names and codes
    raw_data = pd.read_csv('Assignment3Data.csv')
    school_codes = raw_data['School Code'].unique()
    school_names = raw_data['School Name'].unique()

    # Create dictionary of names+codes : index
    school_codes_dict = {str(code):num for (code,num) in zip(school_codes, range(len(school_codes)))}
    school_names_dict = {name:num for (name,num) in zip(school_names, range(len(school_names)))}
    school_index_dict = school_codes_dict | school_names_dict


    # Prompt for user input
    while True:
        try:
            school_index = get_user_input(school_index_dict)
            print(school_data_3D[:,school_index,:])
            break
        except ValueError as err:
            print(err)
            continue

    

    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")
    print("School Name: " + school_names[school_index] + ", School Code: " + str(school_codes[school_index]))
    mean_G10 = sum(school_data_3D[:,school_index,0])/len(years_combined)
    print("Mean enrollment for Grade 10 across all years:", int(mean_G10))
    mean_G11 = sum(school_data_3D[:,school_index,1])/len(years_combined)
    print("Mean enrollment for Grade 11 across all years:", int(mean_G11))
    mean_G12 = sum(school_data_3D[:,school_index,2])/len(years_combined)
    print("Mean enrollment for Grade 12 across all years:", int(mean_G12))
    max_grade = school_data_3D[:,school_index, :].max()
    print("Highest enrollment for any grade across all years:", int(max_grade))
    min_grade = school_data_3D[:,school_index, :].min()
    print("Lowest enrollment for any grade across all years:", int(min_grade))
    total_enrollment_by_year = [sum(school_data_3D[x,school_index,:]) for x in range(len(school_data_3D))]
    total_yearly_enrollment = {year:int(num) for (year,num) in zip(range(2013,2023), total_enrollment_by_year)}
    print("Total enrollment by year:",total_yearly_enrollment)
    print("Total ten year enrollment (2013-2022):", sum(total_yearly_enrollment.values()))
    print("Mean enrollment over the 10 year period (2013-2022):", sum(total_yearly_enrollment.values())//len(school_data_3D))
    x = school_data_3D[:,school_index,:]
    mask_500 = school_data_3D[:,school_index,:] > 500
    if mask_500.any:
        filtered = x[mask_500]
        print("The median value of all enrollments greater than 500:",np.median(filtered))
    else:
        print("No enrollments over 500.")
    
  

   


    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")


if __name__ == '__main__':
    main()

