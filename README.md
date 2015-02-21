# dumpmon-scraper.py

This is a simple script that will open the last 20 links from the [@Dumpmon](https://twitter.com/dumpmon) twitter account, dig through the info, and send an email alert to you based on a keyword or keywords you define. 

## Prerequisites

###  Twitter API Credentials
You'll need to create a new Twitter app at https://apps.twitter.com in order to
get the keys and tokens necessary to scrape the info. 

1. Click "Create New App" and fill out the info
1. After the app is created, look at the "Keys and Access Tokens" tab to
       find the info necessary to run this script
1. Update the variables in the script to your own

###  Python Libraries
You will need to ensure that both the [Python-Twitter](https://github.com/bear/python-twitter) and [Requests](http://docs.python-requests.org) libraries are available to Python.  If you have [pip](https://pip.pypa.io) installed, then simply use:

    sudo pip install python-twitter Requests
    
## Running
./dumpmon-scraper.py

Simple enough :) I have it cron'd, but it can be run adhoc as well
