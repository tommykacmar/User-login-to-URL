#!/usr/bin/python3
#title           :BO_user_login_check.py
#description     :Check to get the url of the website of BO Application behind a login
#author          :tomas.kacmar@dieboldnixdorf.com
#date            :20190712
#version         :1.0
#usage           :python3.4 BO_user_login_check.py
#python_version  :3.4
##########################################################################################


#module requests pulls the data from the url website
import requests
import datetime

#Date def
now = datetime.datetime.now()

#Viariables
url_ok = "https://10.249.64.20:50443/ShellUS-BackOffice/?2"
searching_url = "https://10.249.64.20:50443/ShellUS-BackOffice/wicket/bookmarkable/cz.wincor.eps.backoffice.web.login.LoginPage?0-1.IFormSubmitListener-loginForm"
#url_not_ok = "https://10.249.64.20:50443/ShellUS-BackOffice/wicket/bookmarkable/cz.wincor.eps.backoffice.web.login.LoginPage?1"
#url_code_ok = 200
my_log = datetime.datetime.now().strftime("%Y%m%d")

#definition of user login and password to BO Application
login_data = {
        'password': '*******',
        'userName': '*******'
}

with requests.Session() as s:
   url = searching_url
   r = s.get(url, timeout=10, verify=False)
   r = s.post(url, data=login_data,)
   with open("/tmp/" + my_log + "_BO_user_login_check" '.log', "a") as f:
      if r.url == url_ok:
         print ((now.strftime("%Y-%m-%d %H:%M:%S")), "user successfuly logged into shellUS BO application", r.url, r.status_code, file=f)
      else:
         print ((now.strftime("%Y-%m-%d %H:%M:%S")), "user loging into shellUS BO application error", r.url, r.status_code, file=f)
