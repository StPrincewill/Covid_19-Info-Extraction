# Covid_19-Info-Extraction

In the midst of some much information and data about Covid 19 all over the world, it could be difficult to narrow down covid 19 information for a particular country. What if there is a simple application that could extract this information for a particular country when the user enters the country name? I did this little program to extract covid data from a dataset and display the informtion for the user to see using python and pandas. The data comes from Kaggle.com and is extracted from the Johns Hopkins University site. 

When the program is run, the following Menu display pops up and the user will be expected to enter any of the options to extract the information
                           
                           
           Menu:Choose any of the following Options a - d
a. Current Global Count for Confirmed Cases, Death and Recovered 

b. Country/Region Count for Confirmed Cases, Death and Recovered

c. History of Counts for Confirmed Cases, Death and Recovered for Country/Region

d. Exit

If the user enters a, the current global count of cases, death and recovered is displayed

if the user enters b, it will prompt the user to enter a region or country and it then displays the covid 19 situation of that country

if the user enters c, it prompts the user to enter the country/region and it then displays the history of covid 19 for that country including the date each was reported

if the user enters d, the program is closed

It validates the user input so that If the user enters anything not in the menu, it prompts the user to enter the right input except they want to exit the program

This program will be useful as the dataset continue to pile up and become large where it becomes a challenge to manually extracting data
