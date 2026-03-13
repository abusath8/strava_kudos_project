### Overview
This repository houses a project that is used to call the Strava API to get data on a personal strava account. Documentation for this API is found at https://developers.strava.com/

### Files
#### data-acquisition.py
This file actually calls the API. In order to run this file, the user needs a credentials.py file that houses the user access code. The gathered stats from strava are then saved in a csv file.

#### strava_kudos_data.csv
This is an example of a csv created from running data-acquisition.py. The data is from my public strava account. 