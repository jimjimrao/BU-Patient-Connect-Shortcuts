# BU Patient Connect Shortcuts

## General Info  
I created this program to automate the process of filling out the survey and appointment booking times on the BU patient connect website. It is compatible with Mac and Windows systems.

## Technologies
Project is created with: 

appdirs==1.4.4
certifi==2020.12.5
distlib==0.3.1
filelock==3.0.12
pipenv==2020.11.15
selenium==3.141.0
six==1.15.0
urllib3==1.26.3
virtualenv==20.4.2
virtualenv-clone==0.5.4

## Setup 
To use this project, first install the requirement.txt into your python environment using your shell: 

```
$ pip install -r requirements.txt
```
Now you can run the script from the directory. 

### Optional:
If you want to speed up the process, you can fill in the info.py file with your BU login and password and select your preferred testing center. 

Example of info.py: 

```
#Enter your BU login details in between the quotations if you want to program to auto-login

username = "Rhett"
password = "Terrier"

# Select Default Testing Site by putting the number associated with choice after the equals sign 

# 0 = 808 Gallery-808 Comm Ave
# 1 = Agganis Lobby-925 Comm Ave
# 2 = BUMC-72 E Concord St 
# 3 = Kilachand-610 Comm Ave

# ('choice = 0' means you want 808 Gallery to be your default testing site) 

choice = "1"
```