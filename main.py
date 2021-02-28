#!/usr/bin/env python
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, pyautogui


username = input("Enter your BU username:")
from getpass import getpass
pw = getpass("Enter your password:")



start = time.time()
web = webdriver.Chrome()
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


#Click Survey Button
survey_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl03"]/div[3]/div/a')))
survey_button.click()

#Click Continue Button
time.sleep(0.5)
continue_button = web.find_element_by_xpath('//*[@id="mainbody"]/div[2]/div[1]/div/div[2]/a')
continue_button.click()


time.sleep(0.5)
#Survey Questions
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






