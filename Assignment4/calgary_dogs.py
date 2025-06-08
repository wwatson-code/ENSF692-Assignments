# calgary_dogs.py
# William Watson
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 README file.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import numpy as np
import pandas as pd


def get_user_input(all_data, header):
    """_summary_

    Args:
        all_data (Pandas DF): _description_
        header (string): _description_

    Raises:
        KeyError: _description_

    Returns:
        _type_: _description_
    """    
    input_string = input("Please enter a dog breed: ")
    input_string = input_string.upper()

    if input_string in all_data[header].values:
        return input_string
    else:
        raise KeyError("Dog breed not found in data. Please try again.")
    
def show_breed_stats(all_data, breed):
# print years where breed 
    breed_mask = all_data['Breed'] == breed
    breed_years = all_data['Year'][breed_mask].unique()
    print("The", breed, "was found in the top dog breeds for years", breed_years)

    # Calculate and display the total number of breed registrations in data
    breed_registrations = all_data['Total'][breed_mask]
    print("There have been", np.nansum(breed_registrations), breed, "dogs registered total.")

    # Calculate and display the percentage of registrations year by year
    for year in breed_years:
        year_mask = all_data['Year'] == year
        sum_registrations_year = np.nansum(all_data['Total'][year_mask])
        breed_year_mask = year_mask & breed_mask
        sum_registrations_breed_year = np.nansum(all_data['Total'][breed_year_mask])
        breed_year_registration_ratio = sum_registrations_breed_year / sum_registrations_year
        print(f"The {breed} was {breed_year_registration_ratio:.3%} of top breeds in {year}.")

    # Calculate and display percentage of all registrations total
    all_breeds_total = np.nansum(all_data['Total'])
    this_breed_total = np.nansum(breed_registrations)
    breed_ratio = this_breed_total/all_breeds_total
    print("The",breed, f"was {breed_ratio:.3%} of top breeds across all years.")

    # Display most popular month and year for the breed
    max_idx = breed_registrations.idxmax()
    print(f"The most popular month for {breed} was {all_data['Month'][max_idx]} {all_data['Year'][max_idx]}.")





def main():

    # Import data here
    all_data = pd.read_excel("/Users/williamwatson/VScode-projects/ENSF692/ENSF692-Assignments/Assignment4/CalgaryDogBreeds.xlsx")
    
    print("ENSF 692 Dogs of Calgary")

    # User input stage
    # Prompt for user input
    while True:
        try:
            breed = get_user_input(all_data,'Breed')
            break
        except KeyError as err:
            print(err)
            continue


    # Data anaylsis stage
    show_breed_stats(all_data, breed)
    

if __name__ == '__main__':
    
    main()
