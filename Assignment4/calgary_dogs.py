# calgary_dogs.py
# William Watson
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 README file.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import pandas as pd


def get_user_input(all_data):
    input_string = input("Please enter a dog breed: ")
    input_string = input_string.upper()

    if input_string in all_data['Breed'].values:
        return input_string
    else:
        raise KeyError("Dog breed not found in data. Please try again.")




def main():

    # Import data here
    all_data = pd.read_excel("/Users/williamwatson/VScode-projects/ENSF692/ENSF692-Assignments/Assignment4/CalgaryDogBreeds.xlsx")
    print(all_data)
    


    print("ENSF 692 Dogs of Calgary")

    # User input stage
    # Prompt for user input
    while True:
        try:
            breed = get_user_input(all_data)
            print("good input")
            break
        except KeyError as err:
            print(err)
            continue

    # Data anaylsis stage

    # print years where breed 
    breed_mask = all_data['Breed'] == breed
    breed_years = all_data['Year'][breed_mask].unique()
    print(breed_years)


if __name__ == '__main__':
    
    main()
