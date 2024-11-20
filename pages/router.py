from fastapi import APIRouter
import requests
from bs4 import BeautifulSoup

router = APIRouter(prefix="/pages", tags=["frontend"])

@router.get("/anime_ongoing")
async def get_anime_ongoing():
    url = "https://animego.org/anime/status/ongoing"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"Error": f"Data extraction error. Code: {response.status_code}"}
    
    data = BeautifulSoup(response.text, "html.parser")
    
    result = {}
    
    anime_links = data.find_all("a", href=True)
    
    for index, link in enumerate(anime_links):
        anime_name = link.text.strip()
        anime_link = link["href"]
        
        if "https://animego.org/anime/" not in anime_link or any(forbidden in anime_link for forbidden in ["type", "season", "genre"]):
            continue
        
        if link.get("class") == ["anime-list-lazy", "lazy"] or not anime_name:
            continue
        
        result[index] = {"name": anime_name, "link": anime_link}
    
    return result


@router.get("/anime_latest")
async def get_anime_latest():
    url = "https://animego.org/anime/status/latest"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"Error": f"Data extraction error. Code: {response.status_code}"}
    
    data = BeautifulSoup(response.text, "html.parser")
    
    result = {}
    
    anime_links = data.find_all("a", href=True)
    
    for index, link in enumerate(anime_links):
        anime_name = link.text.strip()
        anime_link = link["href"]
        
        if "https://animego.org/anime/" not in anime_link or any(forbidden in anime_link for forbidden in ["type", "season", "genre"]):
            continue
        
        if link.get("class") == ["anime-list-lazy", "lazy"] or not anime_name:
            continue
        
        result[index] = {"name": anime_name, "link": anime_link}
    
    return result


@router.get("/anime_2023")
async def get_anime_2023():
    url = "https://animego.org/anime/season/2023"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"Error": f"Data extraction error. Code: {response.status_code}"}
    
    data = BeautifulSoup(response.text, "html.parser")
    
    result = {}
    
    anime_links = data.find_all("a", href=True)
    
    for index, link in enumerate(anime_links):
        anime_name = link.text.strip()
        anime_link = link["href"]
        
        if "https://animego.org/anime/" not in anime_link or any(forbidden in anime_link for forbidden in ["type", "season", "genre"]):
            continue
        
        if link.get("class") == ["anime-list-lazy", "lazy"] or not anime_name:
            continue
        
        result[index] = {"name": anime_name, "link": anime_link}
    
    return result