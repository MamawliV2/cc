from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BankCard:
    def __init__(self, card_number, expiry_month, expiry_year, cvv):
        self.card_number = card_number
        self.expiry_month = expiry_month
        self.expiry_year = expiry_year
        self.cvv = cvv

def login_to_site(driver, username, password, login_url):
    driver.get(login_url)
    time.sleep(2)
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "loginButton").click()
    time.sleep(2)

def pay_invoice(driver, card, payment_url):
    driver.get(payment_url)
    time.sleep(2)
    driver.find_element(By.ID, "card_number").send_keys(card.card_number)
    driver.find_element(By.ID, "expiry_month").send_keys(card.expiry_month)
    driver.find_element(By.ID, "expiry_year").send_keys(card.expiry_year)
    driver.find_element(By.ID, "cvv").send_keys(card.cvv)
    driver.find_element(By.ID, "payButton").click()
    time.sleep(2)
    return "Payment successful" in driver.page_source

def read_cards_from_file(file_path):
    cards = []
    with open(file_path, 'r') as file:
        for line in file:
            card_info = line.strip().split('|')
            if len(card_info) == 4:
                cards.append(BankCard(card_info[0], card_info[1], card_info[2], card_info[3]))
    return cards

def main():
    payment_url = input("Enter the payment page URL: ")
    login_url = input("Enter the login page URL: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    cards_file_path = input("Enter the path to the cards file (txt): ")

    cards = read_cards_from_file(cards_file_path)

    driver = webdriver.Chrome()
    login_to_site(driver, username, password, login_url)

    for card in cards:
        if pay_invoice(driver, card, payment_url):
            print(f"Invoice paid successfully with card {card.card_number}")
            break
        else:
            print(f"Failed to pay invoice with card {card.card_number}")

    driver.quit()

if __name__ == "__main__":
    main()
