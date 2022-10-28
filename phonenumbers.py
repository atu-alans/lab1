# Code to display the location of a phone number

# Import the phonenumbers package
import phonenumbers

# Import geocoder from the phonenumbers package
from phonenumbers import geocoder

# Request the user to enter their phone number
userinput = input("Enter the phone number: ")

# Parse the inputted number
phone_number = phonenumbers.parse(userinput)

# Print the location of the number
print("That phone number is from "+ geocoder.description_for_number(phone_number, 'en'))

# Added comment to confirm new branch has been created.
# Added comment to check if Pycharm adds to newly created branch git_commands.
# Added comment to check if Pycharm commits to new branch git_pycharm.