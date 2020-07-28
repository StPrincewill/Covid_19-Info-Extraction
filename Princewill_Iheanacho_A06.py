# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 14:09:48 2020

@author: Dell
"""


import pandas as pd
#import numpy as np


df_covid19 = pd.read_csv('C:\\Users\\Dell\\Desktop\\Python\\covid_19_data.csv')

df_covid19['Confirmed'] = df_covid19['Confirmed'].astype('int')
df_covid19['Deaths'] = df_covid19['Deaths'].astype('int')
df_covid19['Recovered'] = df_covid19['Recovered'].astype('int')


df_covid19 = df_covid19.drop(['SNo','Province/State','Last Update'], axis = 1)


df_covid19_group = df_covid19.groupby(['ObservationDate','Country/Region']).sum().reset_index()


df_covid19_group = df_covid19_group.rename(columns = {"Country/Region":"Country_Region"})

Last_date = df_covid19_group.ObservationDate.sort_values(ascending=True).tail(1).iloc[0]

glob_confirmed = df_covid19_group.loc[df_covid19_group['ObservationDate']==Last_date,'Confirmed'].sum()
glob_deaths = df_covid19_group.loc[df_covid19_group['ObservationDate']==Last_date,'Deaths'].sum()
glob_recovered = df_covid19_group.loc[df_covid19_group['ObservationDate']==Last_date,'Recovered'].sum()






##Function that displays the menu

def menu():
    print("Menu:Choose any of the following Options a - d")
    print("a. Current Global Count for Confirmed Cases, Death and Recovered ")
    print("b. Country/Region Count for Confirmed Cases, Death and Recovered")
    print("c. History of Counts for Confirmed Cases, Death and Recovered for Country/Region")
    print("d. Exit")

    




##Function that display the global count
def display_global():
        
        print('The Current Global Count for Covid19' )
        print('Confirmed Cases:',glob_confirmed, '|', 'Deaths:', glob_deaths, '|','Recovered:', glob_recovered)
        return

##Function that display the Country Count
def display_region():
            region_sum = 0 
            region_death = 0
            region_recvd = 0
            input_country = input('Enter Country/Region : ')
            
            if input_country in df_covid19_group['Country_Region'].unique():
                pass
            else:
                print("Country not valid")
                return
                   
            country_df = df_covid19_group[df_covid19_group["Country_Region"] == input_country]
            region_sum = country_df.sort_values(by=['ObservationDate']).tail(1)['Confirmed']
            region_death = country_df.sort_values(by=['ObservationDate']).tail(1)['Deaths']
            region_recvd = country_df.sort_values(by=['ObservationDate']).tail(1)['Recovered']
            
            print('The Current Count for Covid19 Cases in ', input_country)
            print('Confirmed:',int(region_sum.iloc[0]), '|', 'Deaths:',int(region_death.iloc[0]), '|', 'Recovered:',int(region_recvd.iloc[0]))
            return


##Function that display the Country's History Count
def display_history():
    input_country = input('Enter Country/Region : ')
    
    if input_country in df_covid19_group['Country_Region'].unique():
        pass
    else:
        print("Country not valid")
        return
    country_df = df_covid19_group[df_covid19_group["Country_Region"] == input_country]
    country_df = country_df.drop(['Country_Region'], axis =1)
    print('The History of Counts for Confirmed Cases, Deaths and Recovered for',input_country)
    print(country_df.reset_index(drop=True))
    
   


def option():
    select_option = input("Enter an Option from the Menu: ") 
    return select_option

#Main Program

getinput = None


menu()
while True:
          getinput = option()
          if getinput == 'd':
                break

          elif getinput == 'a':
             display_global()
          elif getinput == 'b':
              display_region()
          elif getinput == 'c':
              display_history()
             
          else:
             print("Invalid choice. Try again.")

print("You have exited the program") 
