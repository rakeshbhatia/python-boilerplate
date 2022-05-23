import time
import random
import requests
import pandas as pd
from bs4 import BeautifulSoup
from multiprocessing import Pool
from multiprocessing import Process
from fake_useragent import UserAgent
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

def scrape():
	ua = UserAgent()
	userAgent = ua.random
	headers = {"User-Agent":userAgent}
	url = "https://google.com"
	data = requests.get(url, headers=headers)
	soup = BeautifulSoup(data.content, "lxml")
	print(soup.body.prettify())

def main():
	scrape()

if __name__ == "__main__":
	main()