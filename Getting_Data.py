# This app , can get Laptop Data (Ram , name , price) 
# Next coed, with name "Pareto_Fron" , can optimize (with the Pareto method) to find most affordable laptops with max Ram   

import mysql.connector
from bs4 import BeautifulSoup
import requests
import re
import random 
from time import sleep

cnx = mysql.connector.connect(user='md', password='M1377mmn',
                              host='127.0.0.1',
                              database='learn')
cursor = cnx.cursor()


Roms = [2,3,4,6,8,10,12,20,24,32,48,64,128]



for j in Roms :
    print("****************")
    print(j)
    
    for i in range(2) :

        delay = random.randint(0, 2)/2
        sleep(delay)
        
        if i == 0 :
            r = requests.get('https://www.zoomit.ir/product/list/laptop/rm-%dgig/sort/16/'%(j))
        else :
            r = requests.get('https://www.zoomit.ir/product/list/laptop/rm-%dgig/sort/16/page/%d/'%(j,i+1))

        soup = BeautifulSoup(r.text,'html.parser')
        Names = soup.find_all("h3", {"class": "productTitle"})
        Prices = soup.find_all("div", {"class": "productSummery__prices--highlited"})

        for i in range (1,(int(len(Prices)/2))):
            price =Prices[2*i].text
            price = int(price[:price.index(',')])+int(price[price.index(',')+1:price.index(',')+4])*0.001
            name = Names[i].text
            print (price)
            print (name)
            print("")
            
            cursor.execute('INSERT INTO laptop VALUES (\'%s\',\'%s\',\'%s\')'%(j,name,price))
            cnx.commit()


cnx.close()
