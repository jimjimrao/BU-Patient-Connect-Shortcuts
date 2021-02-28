
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, pyautogui

username = input("Enter your BU username:")
from getpass import getpass
pw = getpass("Enter your password:")

web = webdriver.Chrome()
web.get('https://www.bu.edu/shs/getting-started/using-patient-connect/')

secure_login_button = web.find_element_by_xpath('//*[@id="post-7513"]/p[2]/a')
secure_login_button.click() 

#find a way to switch tabs 

#Log in Screen
time.sleep(2)
pyautogui.typewrite(username + '\t' + pw + '\t')  #NOTE need to change this so that it doesn't not use key strokes 
pyautogui.press('enter')
print("Logging in...")



web.get('https://patientconnect.bu.edu/Mvc/Patients/QuarantineSurvey')
pyautogui.hotkey('optionleft','command','left')                     #NOTE need to change this so that it doesn't not use key strokes 
pyautogui.press('enter')
survey_button = web.find_element_by_xpath('//*[@id="mainbody"]/div[2]/div[1]/div/div[2]/a')
survey_button.click()
time.sleep(1)
#Survey Questions
web.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[2]/fieldset/div/div[1]/div').click()
web.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[3]/fieldset/div/div[1]/div').click()
web.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[4]/fieldset/div/div[1]/div').click()
web.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[5]/fieldset/div/div[1]/div').click()
web.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[6]/fieldset/div/div[1]/div').click()
web.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[7]/fieldset/div/div[1]/div').click()
web.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[8]/fieldset/div/div[1]/div').click()
web.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[9]/fieldset/div/div[1]/div').click()
#Submit Survey
web.find_element_by_xpath('//*[@id="mainbody"]/footer/div/div[2]/input').click()

print('Survey Submitted')






