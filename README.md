# FOOD TRUCK FINDER
A python (`3.5`) command line interface (CLI) program that displays currently open food trucks in the San Fransisco Area.
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

## Proposal Write-Up - Proof-of-Concept to Production

This simple CLI program, while successfully demostrating proper Scrota API development, leaves much to be needed as a scalable production system. This service is best suited as a browser-based web application. To convert this simple CLI into a scalable app would require a re-write, and ultimately a move from Python to Javascript. This web app could query Socrata API directly from each user's own client browser. My design would use a statically hosted web-page without the need for any additional complex back-end servers. A static site could be hosted on a number of different providers, we can choose between: GitHub Pages, S3 Website, GCP Google Storage, or Heroku. Each provider offers a set of tooling for deploying, monitoring, and controlling the content delivery of our website. For S3 Website, we can also choose to use [CloudFront](https://aws.amazon.com/cloudfront/) for advance caching and improved delivery. Furthermore, while this static site could be written using vanilla html/javascript, I propose we choose a industry supported UI framework such as [ReactJs](https://reactjs.org/). ReactJs allows us build a simple and re-usable component driven UI as a single page app. React project setup/management can be simplified by using Facebook's [Create React App](https://github.com/facebook/create-react-app). To save valuable time, we will choose an existing component library UI toolkit (or one of our companies choosing). There are many to pick: MaterialUI, React Bootstrap, Ant Design, etc.. Any of these libraries will make our website look profession with minimal front-end development effort. I'm most familiar with [AWS S3 Website](https://aws.amazon.com/websites/), React, and [Material UI](https://material-ui.com/), so these would be my personal choices, but any tech should get the done the job well.

### Technical Highlights:
- Hosting: S3 Static Website - 
- UI Framework: ReactJS Components
- UI Library: Material UI Component Library
- Project Setup: Facebook's Create React App

### Proposed Architecture Diagram
![Architecture Diagram](architecture_diagram.png)