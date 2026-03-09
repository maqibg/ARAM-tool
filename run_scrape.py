import os
from apexlol_scraper import scrape_all_champions

cache_dir = "C:\\Users\\Administrator\\.gemini\\antigravity\\scratch\\aram-assistant\\apexlol_cache"
scrape_all_champions(cache_dir)
print("Finished scraping all champions!")
