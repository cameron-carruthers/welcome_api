# WelcomeHome API

> WelcomeHome is a real estate app for those looking for their next home

This REST API is consumed by the mobile app here: https://github.com/cameron-carruthers/welcome-home

## Published App on Expo.io

> To view on phone, download free Expo app and scan QR code

https://expo.io/@clcarruthers/projects/welcomeHome

## Motivation

When looking for houses, I wanted a real estate app with a better user experience

## Technologies Used

- Python
- Flask
- Realtor API
- Heroku

## Usage

To run this repo, you will need to install dependencies and run appropriate scripts.

## Requirements

- Python3
- Get a free API key for the Realtor API here: https://rapidapi.com/apidojo/api/realtor?utm_source=google&utm_medium=cpc&utm_campaign=Alpha&utm_term=realtor%20api_e&gclid=Cj0KCQiA2uH-BRCCARIsAEeef3n6WXwwVVVHPevlB-d0edu5XqITvr-GRBPSgv3YERGr8DPedhfu0qkaAkj7EALw_wcB
- Create a .env with the following code: API_KEY=whateverkeyyoujustreceived

## Development

Executing the code below will install pip3, start a virtual environment, install dependencies, and start the development server.

```
pip3 install pipenv
pipenv shell
pipenv install -r requirements.txt
python app.py

```
