#!/usr/bin/python3
#Task:demonstrate proficiency with the requests HTTP library. 
#The API you target is up to you, but be sure any data that is returned 
#is "normalized" into a format that is easy for users to understand.
#Noelle 12/3/2021

import requests
import json

assets= 'https://rest.coinapi.io/v1/assets'
URL= "http://10.8.228.56:2224/post"

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
    data = requests.get(assets, params=params).json()
    with open ('assets.json', 'w') as f:
        json.dump(data, f)
    return data

def main():

        
    usd_btc_rate()
    requests.post(URL, json=usd_btc_rate())

if __name__ == "__main__":
    main()
