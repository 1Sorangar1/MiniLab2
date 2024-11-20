# API Mini lab Melko Timofey 5030102/20201

This API is designed to provide information about anime from Animego website.

# Application deployment and configuration

## Requirements
    Python 3
    Postman

## Installation
1. Clone the repository:
```
git clone https://github.com/1Sorangar1/MiniLab2.git
```
2. Install requirements
```
pip install -r requirements.txt
```

## Run application

To run the application:

``` uvicorn main:app ```

# Endpoints

## Ongoing Anime
- **Endpoint**: ```/pages/anime_ongoing```
- **Description**: Get 20 latest ongoing anime names and their links on Animego.

## Latest Anime
- **Endpoint**: ```/pages/anime_latest```
-  **Description**: Get 20 latest finished anime names and their links on Animego.

## 2023 Anime
- **Endpoint**: ```/pages/anime_2023```
- **Description**: Get 20 latest added 2023 anime names and their links on Animego.
# Postman

Postman workplace: [click](https://www.postman.com/1sorangar1/minilab2/collection/or4xmfq/requests)