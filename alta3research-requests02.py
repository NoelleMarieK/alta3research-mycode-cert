#!/usr/bin/python3
#Task:demonstrate proficiency with the requests HTTP library. 
#The API you target is up to you, but be sure any data that is returned 
#is "normalized" into a format that is easy for users to understand.
#Noelle 12/3/2021

import requests
import datetime, sys
from pprint import pprint

url = 'https://rest.coinapi.io/v1/exchangerate/BTC?invert=false'
US_BTC = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'

#API Key Function
def get_creds():
    with open("/home/student/coin.creds") as mycreds:
        coincreds = mycreds.read()
    ## remove any "extra" new line feeds on our key
        #coincreds = "apikey=" + coincreds.strip("\n")
        coincreds = coincreds.strip("\n")
    return coincreds

# Pull Bitcoin exchange rate in US dollar now and last week
def usd_btc_rate():
    
    #set request parameters
    params = {'apikey' : get_creds()}
    rates = requests.get(US_BTC, params=params).json()
    print(f"Exchange rate of Bitcoin in USD now:             ${rates['rate']}")
    
    #Pull last weeks exchange rate
    params = {'apikey' : get_creds(), 'time' : last_week()}
    last_week_rates = requests.get(US_BTC, params=params).json()
    print(f"Exchange rate of Bitcoin in USD on {last_week()}:   ${last_week_rates['rate']}") 
    
    #Pull five years exchange rate
    params = {'apikey' : get_creds(), 'time' : five_years()}
    year_rates = requests.get(US_BTC, params=params).json()
    print(f"Exchange rate of Bitcoin in USD on {five_years()}:   ${year_rates['rate']}")

    return

def last_week():
    today = datetime.date.today()
    week_ago = today - datetime.timedelta(days=7)
    week_ago = str(week_ago)
    return week_ago

def five_years():
    today = datetime.date.today()
    years_ago = today - datetime.timedelta(days=5*365)
    years_ago = str(years_ago)
    return years_ago

def main():

        
    usd_btc_rate()
    print("Wow, wish I would have invested years ago!")

if __name__ == "__main__":
    main()
