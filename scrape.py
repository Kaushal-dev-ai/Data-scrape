import requests
from bs4 import BeautifulSoup
import time
import csv
import send_mail
from datetime import date



urls = ["https://finance.yahoo.com/quote/AMZN/","https://finance.yahoo.com/quote/GOOGL/", "https://finance.yahoo.com/quote/MSFT/"]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'}

today = str(date.today()) + ".csv"
csv_file = open(today, 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Stock Title', 'Current Price', 'Previous Close', 'Open', 'Bid', 'Ask', 'Day Range', '52 Week Range', 'Volume'])


for url in urls:
         stock = []

         html_page = requests.get(url, headers=headers)

         soup = BeautifulSoup(html_page.content, 'lxml') 


         stock_title = soup.find_all ("section", class_="container yf-k4z9w")[0].find("h1").text

# print(stock_title)

         current_price = soup.find_all("div", class_="container yf-1tejb6")[0].find("span").get_text()

         stock.append(stock_title)
         stock.append(current_price)

# print(current_price)

         table_info = soup.find_all("div", class_="container yf-gn3zu3")[0].find_all("li")

# write a loop for table for extracting all the values
# for i in range(len(table_info)):
#     print(table_info[i].find_all("span")[0].get_text() + " ------ " + table_info[i].find_all("span")[1].get_text())

         for i in range(0,8):
             #heading = table_info[i].find_all("span")[0].get_text()
             value = table_info[i].find_all("span")[1].get_text()
             stock.append(value)

#print(table_info[0].find_all("span")[0].get_text() + "    " + table_info[0].find_all("span")[1].get_text()) 

             #print(heading + "  :  " + value)
          
         csv_writer.writerow(stock)
         time.sleep(5)
         
csv_file.close()

send_mail.send(filename=today)



