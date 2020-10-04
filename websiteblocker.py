import time
from datetime import datetime as dt

host_path="C:\Windows\System32\drivers\etc\hosts.txt"
redirect_path="127.0.0.1"
website=['facebook.com','www.facebook.com']
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,13)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,15):
        with open(host_path,'r+') as file:
            content=file.read()
            for website_link in website:
                if website_link in content:
                    pass
                else:
                    file.write(redirect_path+ "" + website_link +"\n")
        print("The websites are blocked")
        break
    else:
        with open(host_path,'r+')as file:
            content= file.readlines()
            file.seek(0)

            for line in content:

                if not any(website_link in line  for website_link in website):
                    file.write(line)
            file.truncate()
        print("websites are unblocked")
        break