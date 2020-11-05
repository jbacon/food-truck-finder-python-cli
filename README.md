# FOOD TRUCK FINDER
A python (`3.5`) command line interface (CLI) program that displays currently open food trucks in San Fransisco Area.
The program queries the Scrota API for the San Fransisco dataset [Mobile Food Truck Schedules](https://dev.socrata.com/foundry/data.sfgov.org/jjew-r69b).


## TL;DR
```bash
pip3 install -r requirements.txt
python3 show_open_food_trucks.py
```

## Prefer Docker?

### Build
```bash
docker build -t food-truck-finder:latest .
```
### Run
```bash
docker run -i food-truck-finder:latest
```

## Future Work...

To convert this simple CLI service into a browser-based web application requires a re-write. My design would involve a simple staticly hosted website (pure html/javascript). No need for any complex backend API server. The Socrata API can be queried directly from client browsers via Javascript. I would choose S3 or GCS to host static website files.