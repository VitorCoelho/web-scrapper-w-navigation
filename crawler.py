import requests
import csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

# URL for the page containing the list of companies
url_base = 'http://www.target.org.br/association/stores'

# Makes a request to the base URL
response = requests.get(url_base)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

# Finds all the company URLs
company_urls = soup.find_all('a', class_='btn btn-primary btn-md px-3')

# Opens the CSV file to write
csv_file = open('company_data.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Nome da Empresa', 'Endereço', 'Cidade', 'Estado', 'CEP', 'Fone', 'Email', 'Homepage'])

# Loop to visit each company URL and extract the data
for company_url in company_urls:
    relative_url = company_url['href']  # Gets the relative URL for each company
    url = urljoin(url_base, relative_url)  # Constructs the absolute URL
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

    # Extracts the company data
    company_name = soup.find('h1', class_='terciary-color').text.strip()

    # Extracts the company information
    company_info = soup.find('div', class_='col-lg-8 conteudo')
    company_info_text = company_info.get_text(separator='\n')

    # Extracts the required fields using regular expressions
    address_match = re.search(r'Endereço:\s*(.*?)\s+', company_info_text)
    address = address_match.group(1) if address_match else ''
    city_match = re.search(r'Cidade:\s*(.*?)\s+', company_info_text)
    city = city_match.group(1) if city_match else ''
    state_match = re.search(r'Estado:\s*(.*?)\s+', company_info_text)
    state = state_match.group(1) if state_match else ''
    cep_match = re.search(r'CEP:\s*(.*?)\s+', company_info_text)
    cep = cep_match.group(1) if cep_match else ''
    phone_match = re.search(r'Fone:\s*(.*?)\s+', company_info_text)
    phone = phone_match.group(1) if phone_match else ''
    email_match = re.search(r'Email:\s*(.*?)\s+', company_info_text)
    email = email_match.group(1) if email_match else ''
    homepage_match = re.search(r'Homepage:\s*(.*?)\s+', company_info_text)
    homepage = homepage_match.group(1) if homepage_match else ''

    # Writes the data to the CSV file
    csv_writer.writerow([company_name, address, city, state, cep, phone, email, homepage])

# Closes the CSV file
csv_file.close()
