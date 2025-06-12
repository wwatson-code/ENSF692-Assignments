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


def get_user_input(data_multi_index, header):
    """ Gets the user input and checks that the input is a member of the specified data column.

    Args:
        all_data (Pandas DF): Pandas dataframe containing data for user input to be checked against.
        header (string): The header of the column to check for membership against the user input

    Raises:
        KeyError: If user input does not exist in specified header column.

    Returns:
        string: The valid user input value as an upper case string.
    """    



    input_string = input("Please enter a dog breed: ")
    input_string = input_string.upper()
    valid_breeds = data_multi_index.index.get_level_values(header).unique().tolist()


    if input_string in valid_breeds:
        return input_string
    else:
        raise KeyError("Dog breed not found in data. Please try again.")
    
    
def show_breed_stats(data_multi_index, breed):
    """ Calculates and displays the following statistics for a specified breed:
        - Years where breed is present in the Dataframe.
        - Total number of registrations for the breed.
        - Percentage of total yearly registrations contributed by the breed.
        - Percentage of total overall registrations contributed by the breed.
        - Month/Year of highest number of registrations for the breed.
    
    Args:
        all_data (Pandas DF): The dataframe containing Year, Month, Breed, and Total (breed registrations that month).
        breed (string): The user specified breed.
    """    
# print years where breed is present
    breed_years = data_multi_index.loc[breed].index.unique().tolist()

    print("The", breed, "was found in the top dog breeds for years", breed_years)


    # Calculate and display the total number of breed registrations in data
    # breed_registrations = all_data['Total'][breed_mask]
    breed_reg_list = data_multi_index.loc[breed]['Total'].values
    print("There have been", np.nansum(breed_reg_list), breed, "dogs registered total.")

    # Calculate and display the percentage of registrations year by year
    for year in breed_years:
        # year_reg_list = data_multi_index.xs(year, level='Year')['Total'].values
        year_mask = data_multi_index.index.get_level_values('Year') == year
        year_reg_list = data_multi_index.loc[year_mask, 'Total'].values
        sum_reg_year = np.nansum(year_reg_list)
        breed_year_reg_list = data_multi_index.loc[breed,year]['Total'].values
        sum_breed_year = np.nansum(breed_year_reg_list)
        breed_year_reg_ratio = sum_breed_year / sum_reg_year
        print(f"The {breed} was {breed_year_reg_ratio:.3%} of top breeds in {year}.")

    # Calculate and display percentage of all registrations total
    all_breeds_total = np.nansum(data_multi_index['Total'].values)
    this_breed_total = np.nansum(breed_reg_list)
    breed_ratio = this_breed_total/all_breeds_total
    print("The",breed, f"was {breed_ratio:.3%} of top breeds across all years.")

    # Display most popular month and year for the breed
    # max_idx = breed_reg_list.max()
    df_reset = data_multi_index.reset_index()
    data_multi_index = df_reset.set_index(['Breed','Year','Month'])
    max_idx = data_multi_index['Total'].idxmax()

    max_year = max_idx[1]
    max_month = max_idx[2]


    print(f"The most popular month for {breed} was {max_month} {max_year}.")





def main():

    # Import data here
    all_data = pd.read_excel("/Users/williamwatson/VScode-projects/ENSF692/ENSF692-Assignments/Assignment4/CalgaryDogBreeds.xlsx")
    #print(all_data)
    data_multi_index = all_data.set_index(['Breed', 'Year'])
    # print(data_multi_index)
    # print(data_multi_index.index.get_level_values('Breed').unique().tolist())
    # if 'LABRADOR RETR' in data_multi_index.index.get_level_values('Breed').unique().tolist():
    #     print("working!")


    #print(all_data[0])
    print("ENSF 692 Dogs of Calgary")

    # User input stage
    # Prompt for user input
    while True:
        try:
            breed = get_user_input(data_multi_index,'Breed')
            break
        except KeyError as err:
            print(err)
            continue


    # Data anaylsis stage
    show_breed_stats(data_multi_index, breed)
    

if __name__ == '__main__':
    
    main()
