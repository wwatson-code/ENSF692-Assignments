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

# Array of given 1D year arrays 
years_combined = np.array([year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022])
    
# Global variable containing the 3D array [Years, School Name, and Grade]
global school_data_3D
school_data_3D = years_combined.reshape(10,20,3)

# Extract unique lists of names and codes, stored in global variables
raw_data = pd.read_csv('Assignment3Data.csv')
global school_codes
global school_names
school_codes = raw_data['School Code'].unique()
school_names = raw_data['School Name'].unique()

# Create global dictionary of {names+codes : index}
school_codes_dict = {str(code):num for (code,num) in zip(school_codes, range(len(school_codes)))}
school_names_dict = {name:num for (name,num) in zip(school_names, range(len(school_names)))}
global school_index_dict
school_index_dict = school_codes_dict | school_names_dict





def get_user_input():
    """
    Get user input as a school name or code.

    Raises:
        ValueError: When user input is not a valid school name or code

    Returns:
        int: The index representing the school in the 3D array
    """
    user_input = input(" Enter School name or code here (e.g. 'Centennial High School' or '1224'): ")
    if user_input in school_index_dict.keys():
        return school_index_dict[user_input]
    else:
        raise ValueError("You must enter a valid school name or code")
    

class School:
    """
    Represents a school with a school name, school code, and index to slice the 3D array. 
    Contains one method to calculate and print a pre-described set of aggregate statistics of the school.
    """
    def __init__(self, name, code, index):

        self.index = index
        self.name = name
        self.code = code
        
   

    def get_school_stats(self):
        """
        Calculates and prints out the following school specific aggregate stats:
        - the mean yearly enrollment for each grade
        - Highest and lowest enrollments for any grade in any year
        - Yearly enrollment totals
        - Total enrollment for the 10 year period
        - Mean annual enrollment for the 10 year period
        - Median value of all grade enrollments greater than 500 (if any)
        """
        print("\n***Requested School Statistics***\n")
        print("School Name: " + self.name + ", School Code: " + str(self.code))
        mean_G10 = np.nanmean(school_data_3D[:,self.index,0])
        print("Mean enrollment for Grade 10:", int(mean_G10))
        mean_G11 = np.nanmean(school_data_3D[:,self.index,1])
        print("Mean enrollment for Grade 11:", int(mean_G11))
        mean_G12 = np.nanmean(school_data_3D[:,self.index,2])
        print("Mean enrollment for Grade 12:", int(mean_G12))
        max_grade = np.nanmax(school_data_3D[:,self.index, :])
        print("Highest enrollment for a single grade:", int(max_grade))
        min_grade = np.nanmin(school_data_3D[:,self.index, :])
        print("Lowest enrollment for a single grade:", int(min_grade))
        total_enrollment_by_year = [np.nansum(school_data_3D[x,self.index,:]) for x in range(len(school_data_3D))]
        total_yearly_enrollment = {year:int(num) for (year,num) in zip(range(2013,2023), total_enrollment_by_year)}
        #print("Total enrollment by year:",total_yearly_enrollment)
        for key in total_yearly_enrollment.keys():
            print("Total enrollment for", key,":",total_yearly_enrollment[key])
        print("Total ten year enrollment:", int(np.nansum(school_data_3D[:,self.index,:])))
        print("Mean total enrollment over 10 years:", int(np.nansum(school_data_3D[:,self.index,:])//len(school_data_3D)))
        school_slice = school_data_3D[:,self.index,:]
        mask_500 = school_data_3D[:,self.index,:] > 500  # create mask
        if mask_500.any():   
            filtered = school_slice[mask_500]   # apply mask
            print("For all enrollments over 500, the median value was:",int(np.nanmedian(filtered)))
        else:
            print("No enrollments over 500.")
    


def get_general_stats():
    """
    Calculates and prints the following general aggregate statistics:
    - mean enrollment in 2013 and 2022
    - total number of graduating students in 2022
    - highest and lowest enrollments for any single grade in the time period
    """
    mean_2013 = int(np.nanmean(school_data_3D[0,:,:]))
    print("Mean enrollment in 2013:", mean_2013)
    mean_2022 = int(np.nanmean(school_data_3D[-1,:,:]))
    print("Mean enrollment in 2022:", mean_2022)   
    total_G12 = int(np.nansum(school_data_3D[-1,:,-1]))
    print("Total graduating class of 2022:", total_G12)
    single_grade_max = int(np.nanmax(school_data_3D))
    print("Highest enrollment for a single grade:", single_grade_max)
    single_grade_min = int(np.nanmin(school_data_3D))
    print("Lowest enrollment for a single grade:", single_grade_min)




def main():
    print("")
    print("***** ENSF 692 School Enrollment Statistics *****")
    print("")
    # Print Stage 1 requirements here
    
    print("Shape of full data array: ",school_data_3D.shape)
    print("Dimensions of full data array:",school_data_3D.ndim)





    # Prompt for user input
    while True:
        try:
            index = get_user_input()
            break
        except ValueError as err:
            print(err)
            continue

    # Create class instance and call method to get stats
    current_school = School(school_names[index], school_codes[index], index)
    current_school.get_school_stats()
   


    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")
    # Get city-wide aggregate stats
    get_general_stats()

if __name__ == '__main__':
    main()

