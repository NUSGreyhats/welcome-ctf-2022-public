from selenium import webdriver
from constants import COOKIE
import multiprocessing
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--incognito")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")

processes = []

def visit(link: str) -> str:
    """Visit the website"""
    p = multiprocessing.Process(target=_visit, args=(link,))
    p.start()
    processes.append(p)
    return f"Visiting {link}"

def _visit(link: str) -> str:
    """Visit the website"""
    with webdriver.Chrome(ChromeDriverManager().install(), options=options) as driver:
        try:
            driver.get(link)
            cookie = {"name": "flag", "value": COOKIE["flag"]}
            driver.add_cookie(cookie)
            driver.get(link)
            return f"Visited {link}"
        except:
            return f"Connection Error: {link}"