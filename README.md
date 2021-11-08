# youtube_scraper
YouTube scraper, a microservice, that can be connected through python socket to search for YouTube video title and url of a movie trailer on YouTube.

Introduction

    This project includes 3 files:
    - youtube_scraper.py         			(This implements the youtube scraper microservice)
    - server.py                             (**credit:** (https://github.com/longmach/IMDB_scraper/blob/main/socket_server.py))
    - client.py                             (**credit:** (https://github.com/longmach/IMDB_scraper/blob/main/socket_client.py))
	
Requirements

  1. Unzip the files in your testing environment.

Testing

  1. Open the 'youtube_microservice' folder in VScode
  2. In the file 'youtube_scraper.py' on line 6 paste the api key I messaged you then save the file
  3. Open a terminal for server and run:
     - python3 server.py
  4. Open another terminal for client and run:
     - python3 client.py

Packages

  - pip3 install beautifulsoup4
  - pip3 install python-dotenv
  - pip3 install google-api-python-client

