import os
from time import sleep
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


URL = "" #  
MAIL = ""  #  Your mail 
PASS = ""  #  Your password
IMAGE_PATH = "" #  Whith outh first / for the path, just Linux Exaple: "home/astaroth/Pictures/image to upload.jpeg"
SUBJECT = ""  #  The Subject
SELECT = "" #  The image to select just the name, will fix in future features  Exaple: "image to upload.jpeg"
FLAG = True #  For check the content and 
INDICATOR = 15  #  Like it's just for myself this is to check how many time will write a email "Total emails/7 7=is the total per mail
file = "" #  Exaple "emails.txt"
TIMER =  #  For ckeck that everything is okay, format for the first mail, after this just coppy all the text


def getting():
    file = open(file, "r")
    lines = file.readlines()
    mails = []
    for line in lines:
        mails.append(line)
    file.close()
    mails[:] = (value.replace('"', "") for value in mails)
    mails[:] = (value.replace(' ', "") for value in mails)
    mails[:] = (value.replace('\n', "") for value in mails)
    mails = list(filter(None, mails))
    return mails


def select(path):
    a = path.split('/')
    sleep(2)
    for v in a:
        pyautogui.hotkey('shift', '/')
        pyautogui.write(v)
    sleep(1)
    pyautogui.press('enter')


def scripting():

    global FLAG
    mails = getting()

    # Session, mail and pass
    driver = webdriver.Chrome()
    driver.get(URL)
    sleep(3)
    mail = driver.find_element(By.ID, "rcmloginuser")
    password = driver.find_element(By.ID, "rcmloginpwd")
    mail.send_keys(MAIL)
    password.send_keys(PASS)
    driver.find_element(By.ID, "rcmloginsubmit").click()
    sleep(2)
    op = 0
    while op < INDICATOR:
        driver.find_element(By.ID, "rcmbtn112").click()  # Select new mail
        sleep(2)

        # To
        dest = driver.find_element(By.ID, "_to")
        driver.find_element(By.ID, "bcc-link").click()
        sleep(1)
        driver.maximize_window()
        # First mail
        dest.send_keys(mails.pop(0))
        # Others
        a = 0
        while a < 6:
            driver.find_element(By.ID, "_bcc").send_keys(mails.pop(0) + " ")
            a += 1

        # Subject
        driver.find_element(By.ID, "compose-subject").send_keys(SUBJECT)

        # Body
        driver.switch_to.frame(driver.find_element(By.ID, "composebody_ifr"))
        os.system("echo %s| clip")
        driver.find_element(By.ID, "tinymce").send_keys(Keys.CONTROL, 'v')
        driver.switch_to.default_content()
        # For check the body
        if FLAG is True:
            sleep(TIMER)
            FLAG = False

        # Image
        driver.find_element(By.ID, "mceu_22").click()
        driver.find_element(By.ID, "mceu_43-action").click()
        sleep(1)
        driver.find_element(By.ID, "image-upload-button").click()
        select(IMAGE_PATH)  # Selecting image
        sleep(2)
        driver.find_element(By.XPATH, "//img[@title='Preguntale al experto.jpeg']").click()
        sleep(1)
        driver.find_element(By.ID, "mceu_50").click()

        driver.find_element(By.ID, "rcmbtn109").click()  # Send Button
        sleep(5)
        op += 1


if __name__ == '__main__':
    scripting()
