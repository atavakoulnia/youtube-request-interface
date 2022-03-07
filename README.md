# YouTube Scraper
A micro-service, connected through sockets with Python, where users can search for videos on YouTube's database

## Introduction 
> This project includes 3 files:
> youtube_scraper.py				(This implements the youtube scraper microservice)
> 
> server.py					(**credit:** (https://github.com/longmach/IMDB_scraper/blob/main/socket_server.py))
> 
> client.py					(**credit:** (https://github.com/longmach/IMDB_scraper/blob/main/socket_client.py))
> 
	
## Requirements
- YouTube API Key

## How to Setup
- Unzip the files in your testing environment
- Open the 'youtube_microservice' folder in VScode
- In the file 'youtube_scraper.py' on line 6 paste your api key
- Install packages
- Open a terminal for server and run: ``` python3 server.py ```
- Open a second terminal for client and run: ``` python3 client.py ```

## Packages
- pip3 install beautifulsoup4
- pip3 install python-dotenv
- pip3 install google-api-python-client
