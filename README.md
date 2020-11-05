# Python Food Truck Finder
Python (`3.5`) command line program that displays currently open food trucks in San Fransico Area.
The program queries the Scrota API of a San Fransico dataset [Mobile Food Truck Schedules](https://dev.socrata.com/foundry/data.sfgov.org/jjew-r69b).


## TL;DR
```bash
pip3 install -r requirements.txt
python3 show_open_food_trucks.py
```

## Via Docker

## Build
```bash
docker build -t food-truck-finder:latest .
```
## Run
```bash
docker run -i food-truck-finder:latest
```

### Future Productionization?

To convert this simple CLI service into a browser-based web application, requires a re-write. My design would involve a simple staticly hosted website (pure html/javascript). No need for any complex backend API server. The Socrata API can be queried directly from client browsers. I would choose S3 or GCS to host static website files.