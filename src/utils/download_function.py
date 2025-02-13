import os
from utils.custom_log import *
from selenium.webdriver.common.by import By
import requests

def download_csv(driver):
    '''
    Downloads a CSV file from a web page using the provided Selenium WebDriver instance.

    This function locates a download button on the page, extracts the download link,
    and saves the CSV file to a specified directory. If the directory does not exist,
    it will be created automatically.
    '''
    
    # Locates the download button and get the link
    download_btn = driver.find_element(By.XPATH, '//a[text()="Download Favorite Foods Spreadsheet"]')
    link = download_btn.get_attribute('href')
    print(link)

    # Directory where the file will be saved
    csv_directory = r'C:\Users\guilh\Documents\Compass\Sprint 4\sprint4_atividade4_Guilherme_Sartori\online_grocery_ordering\python\data'
    
    csv_file_name = 'shopping-list.csv'

    # Downloads the file
    response = requests.get(link, allow_redirects=True)

    # Creates the directory, if it does not exist
    os.makedirs(csv_directory, exist_ok=True)
    output_path = os.path.join(csv_directory, csv_file_name)

    # Saves the file in the specified directory
    with open(output_path, 'wb') as file:
        file.write(response.content)
    log_append(f'Arquivo baixado e salvo em: {output_path}')