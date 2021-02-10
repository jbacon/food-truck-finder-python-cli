#!/usr/bin/env python

import requests
import sys
import os
from datetime import datetime


def main(argv):
    print("Open food trucks...")
    page = 1
    while True:
        data = get_data(page, datetime.now())
        for row in data:
            print("{:<30} {:<30}".format(row["applicant"], row["location"]))
        page += 1
        input("Press Enter for more trucks...")

def get_data(page, currentDatetime):
    url = "http://data.sfgov.org/resource/bbb8-hzi6.json"
    currentTime24 = currentDatetime.strftime("%H:%M")
    params = {
        "$limit": 10,
        "$offset": 10*(page-1),
        "$order": "applicant",
        "dayorder": currentDatetime.today().weekday(),
        "$where": "'{0}' BETWEEN start24 AND end24".format(currentTime24)
    }
    headers = None
    response = requests.get(url, params=params, headers=headers)
    json = response.json()
    if response.status_code == 200:
        return json
    raise Exception("Receive non-200 response from API", response.json())

if __name__ == "__main__":
    main(sys.argv)