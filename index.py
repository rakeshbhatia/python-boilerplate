import json
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
	url = "https://scraping-interview.onrender.com/placeholder_carrier/f02dkl4e/policies/1"
	data = requests.get(url, headers=headers)
	soup = BeautifulSoup(data.content, "lxml")
	tables = pd.read_html(soup.prettify())
	df = tables[0]
	policies = []

	policy_data = []
	for i in range(len(df)):
		policy_dict = {"Id":"", "Premium":"", "Status":"", "Effective Date":"", "Termination Date":""}
		policy_dict["Id"] = df.loc[i, "Id"]
		policy_dict["Premium"] = df.loc[i, "Premium"]
		policy_dict["Status"] = df.loc[i, "Status"]
		policy_dict["Effective Date"] = df.loc[i, "Effective Date"]
		policy_dict["Termination Date"] = df.loc[i, "Termination Date"]
		print(policy_dict)
		policy_data.append(json.dumps(policy_dict))
	policies.append(policy_data)

	customer_card = soup.find_all("div", attrs={"class":"card-body"})[1]

	customer_details = customer_card.find_all("div")

	customer_data = []
	for element in customer_details:
		customer_data.append(element.text.split(":")[1].strip())
	#print(customer_data)

	agent_card = soup.find_all("div", attrs={"class":"card-body"})[0]
	#print(agent_card)

	agent_details = agent_card.find_all("div")
	#print(agent_details)

	agent_data = []
	for element in agent_details:
		agent_data.append(element.text.split(":")[1].strip())
	#print(agent_data)

	ua = UserAgent()
	userAgent = ua.random
	headers = {"User-Agent":userAgent}
	url = "https://scraping-interview.onrender.com/mock_indemnity/a0dfjw9a"
	data = requests.get(url, headers=headers)
	soup = BeautifulSoup(data.content, "lxml")

	policy_list = soup.find("ul", attrs={"id":"policy-list"}).find_all("li")
	
	policy_data = []
	for element in policy_list:
		policy_dict = {"Id":"", "Premium":"", "Status":"", "Effective Date":"", "Termination Date":"", "Last Payment Date":""}
		data = []
		container = element.find("div")
		rows = container.find_all("div")
		for row in rows:
			columns = row.find_all("div")
			for column in columns:
				data.append(column.text.split(":")[1].strip())
		policy_dict["Id"], policy_dict["Premium"], policy_dict["Status"] = data[0], data[1], data[2]
		policy_dict["Effective Date"], policy_dict["Termination Date"], policy_dict["Last Payment Date"] = data[3], data[4], data[5]
		policy_data.append(json.dumps(policy_dict))
	#print(policy_data)

	policies.append(policy_data)

	cards = soup.find_all("div", attrs={"class":"card-body"})

	customer_details = cards[1].find_all("dd")
	#print(customer_details)

	customer_data = []
	for element in customer_details:
		customer_data.append(element.text)
	#print(customer_data)

	agent_details = cards[0].find_all("dd")
	#print(agent_details)

	agent_data = []
	for element in agent_details:
		agent_data.append(element.text)
	#print(agent_data)

	print(policies)

def main():
	scrape()

if __name__ == "__main__":
	main()