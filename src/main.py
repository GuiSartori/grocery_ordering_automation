# Import the libraries needed to find elements and manipulate the browser
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
import os
from dotenv import load_dotenv
from utils.aa_login import login_aa
from utils.download_function import download_csv

# Import exceptions
from selenium.common.exceptions import *

# Import custom log function
from utils.custom_log import *

# Import data functions
from utils.data_utils import *

# Import xlsx data | Aqui fiquei em dúvida se colocaria a importação dos dados dentro do try, mas vi indicação de boa prática para fazer a importação junto aos imports das libs
data_path = r"data\shopping-list.csv"

# Loads the .env file variables to login on AA Community
load_dotenv()
login = os.getenv('login')
senha = os.getenv('senha')

def main():
    
    # Tries to create the log, open the web browser and start the RPA Challenge
    try:

        # Get the name of the python file that is being executed to create the log folder
        nome_arquivo_py = os.path.basename(__file__).replace('.py', '')

        # Creates the log
        log_create(nome_arquivo_py)
        log_append("Início do desafio Online Grocery Ordering")

        # Initializes the driver (in this case, Edge)
        edge_driver = r"src\utils\msedgedriver.exe"
        driver = webdriver.Edge(edge_driver)

        # Opens the desired page and maximizes the window
        driver.get("https://pathfinder.automationanywhere.com/challenges/AutomationAnywhereLabs-ShoppingList.html?")
        driver.maximize_window()
        log_append("Navegador inicializado na página do desafio Online Grocery Ordering ")

        # The login_aa function performs the login for Automation Anywhere Community
        login_aa(driver,login,senha)
    
        time.sleep(3)
        log_append("Iniciando preenchimento da lista de compras")
        
        # Loading csv file
        if os.path.exists(data_path):
            log_append("Arquivo csv encontrado")
        else:
            log_append("Arquivo csv não encontrado")
            download_csv(driver)
        
        df = load_csv(data_path)
        log_append("Dados do arquivo csv carregados com sucesso")
        
        for index, row in df.iterrows():
            
            # Adds the "Favorite Food" item of the row to the input field   
            item_input_field = driver.find_element(By.XPATH, '//*[@id="myInput"]')
            item_input_field.send_keys(row['Favorite Food'])
            
            # Clicks the "Add Item" button
            add_btn = driver.find_element(By.XPATH, '//*[@id="add_button"]')
            add_btn.click()
            log_append(f"{row['Favorite Food']} adcionado à lista de compras com sucesso")
        
        # Clicks on the radio selection to agree with the terms      
        agree_selector = driver.find_element(By.XPATH, '//*[@id="agreeToTermsYes"]')
        agree_selector.click()
        log_append("Realizado o click para confirmar a aceitação dos termos de consentimento")
        
        # Clicks the submit button
        submit_btn = driver.find_element(By.XPATH, '//*[@id="submit_button"]')
        submit_btn.click()
        log_append("Realizado o click no botão de Submit Order")
        
        time.sleep(3)
        log_append("Tarefa realizada com sucesso")
        
        # Capturing the results of the bot execution
        success_message = driver.find_element(By.XPATH, '//*[@id="success-title"]').text
        processing_time = driver.find_element(By.XPATH, '//*[@id="processing-time"]').text
        accuracy = driver.find_element(By.XPATH, '//*[@id="accuracy"]').text
        log_append(f"Mensagem: {success_message} | Tempo de processamento: {processing_time} | Acurácia: {accuracy}")
        
    except Exception as e:
            log_append(f"Ocorreu um erro - {e.__class__.__name__}")

    log_append("Finalizando execução do bot")

# Performs the main function
main()