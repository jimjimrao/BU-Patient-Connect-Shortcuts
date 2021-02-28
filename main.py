#!/usr/bin/env python
import selenium, time, os, platform
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass

#Enter username and password between the quotations to auto log in 
username = ""
pw = ""

if username =="":
    username = input("Enter your BU username:")
if pw =="":
    pw = getpass("Enter your password:")

#check operating system (windows or mac)
osys = platform.system()

if osys == 'Windows':
    PATH = "C:\Program Files (x86)\ChromeDriver\chromedriver.exe"
    web = webdriver.Chrome(PATH)

elif osys == 'Darwin':
    web = webdriver.Chrome()
# make sure this path is correct

start = time.time()

web.get('https://www.bu.edu/shs/getting-started/using-patient-connect/')
wait = WebDriverWait(web,10)

wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="post-7513"]/p[2]/a'))).click()

#switch tabs 
web.switch_to.window(web.window_handles[1])

#Log in Screen
username_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="j_username"]')))
username_input.send_keys(username)

pw_input = web.find_element_by_xpath('//*[@id="j_password"]')
pw_input.send_keys(pw)

login_button = web.find_element_by_xpath('/html/body/div[1]/div/form/button')
login_button.click()

print("Logging in...")

# # #Click Survey Button

survey_button = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Complete Survey'))
        )

survey_button.click()

#Click Continue Button
time.sleep(0.5)
continue_button = wait.until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="mainbody"]/div[2]/div[1]/div/div[2]/a'))
        )
continue_button.click()



#Survey Questions
time.sleep(0.5)
web.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[2]/fieldset/div/div[1]/div').click()
web.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[3]/fieldset/div/div[1]/div').click()
web.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[4]/fieldset/div/div[1]/div').click()
web.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[5]/fieldset/div/div[1]/div').click()
web.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[6]/fieldset/div/div[1]/div').click()
web.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[7]/fieldset/div/div[1]/div').click()
web.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[8]/fieldset/div/div[1]/div').click()
web.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[9]/fieldset/div/div[1]/div').click()
print('Survey Complete')

#Submit Survey
web.find_element_by_xpath('//*[@id="mainbody"]/footer/div/div[2]/input').click()
print('Survey Submitted')
print('This took: %.2f seconds' % (time.time()-start))
