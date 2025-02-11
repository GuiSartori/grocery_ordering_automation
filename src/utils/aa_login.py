from selenium.webdriver.common.by import By
import time
from utils.custom_log import log_append

def login_aa(driver,login,senha):
    '''
    Performs the login process on the Automation Anywhere (AA) Community website.

    This function automates the login process by:
    - Accepting cookies.
    - Clicking the "Community login" button.
    - Filling in the email and password fields.
    - Submitting the login form.
    '''
    time.sleep(3) # Waits the button to accept the cookies
    
    # Clicks the Accept All Cookies button
    cookie_btn = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
    cookie_btn.click()
    log_append("Realizado click no botão Accept All Cookies")

    # Clicks the Community login button
    community_login_btn = driver.find_element(By.XPATH, '//button[text()="Community login"]')
    community_login_btn.click()
    log_append("Realizado click no botão de login no AA Community")

    # Fill in the data and executes the login
    time.sleep(3)
    email_field = driver.find_element(By.XPATH, '//input[@placeholder="*Email"]')
    email_field.send_keys(login)

    # Click the Next button
    next_btn = driver.find_element(By.XPATH, '//button[text()="Next"]')
    next_btn.click()
    time.sleep(1)
    
    # Fill in the password field
    password_field = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
    password_field.send_keys(senha)

    # Click the Log in button
    log_in_btn = driver.find_element(By.XPATH, '//button[text()="Log in"]')
    log_in_btn.click()
    log_append("Login no Automation Anywhere Community realizado com sucesso")