# YouTube Scraper
A micro-service, connected through sockets with Python, where users can search for videos on YouTube's database.

## Introduction 

    This project includes 3 files:
    - youtube_scraper.py         			(This implements the YouTube scraper microservice)
    - socket_server.py
    - socket_client.py
	
## Requirements
- YouTube API Key

## Setup
- Unzip the files in your testing environment
- Open the 'youtube_microservice' folder in VScode
- In the file 'youtube_scraper.py' on line 6 paste your api key
- Install packages

## How to Run
- Open a terminal for server and run: ``` python3 server.py ```
- Open a second terminal for client and run: ``` python3 client.py ```
- Finally, run ``` flask run ``` to run the program

## Packages
- ``` pip3 install beautifulsoup4 ```
- ``` pip3 install python-dotenv ```
- ``` pip3 install google-api-python-client ```
- ``` pip3 install flask ```

## Scraper Demonstration

<img width="419" alt="Example" src="https://user-images.githubusercontent.com/71794386/140621920-e4b1406f-6b61-481c-8561-49045c123b08.png">
