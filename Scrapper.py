import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.ca/gp/product/B00KK9481I/ref=ox_sc_act_title_1?smid=A3DWYIK6Y9EEQB&psc=1'

headers = {"User-Agent":'Mozilla / 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 79.0.3945.88 Safari / 537.36' }


def check_price():
    # This code returns all the data from the website we are calling from
    page = requests.get(URL, headers=headers)

    # This gives you the product title of the ite  m you are looking for
    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id="productTitle").get_text()

    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[5:12])

    print(title.strip())
    print(converted_price)

    if (converted_price < 40):
        send_mail()


def send_mail():
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('kalitoosinde@gmail.com', 'pyfwgyqehznwhquu')

    subject = 'Price Fell Down'
    body = 'Check the amazon link:https://www.amazon.ca/gp/product/B00KK9481I/ref=ox_sc_act_title_1?smid=A3DWYIK6Y9EEQB&psc=1'

    msg = "%s %s" % ({subject}, {body})  # f'Subject: {subject}\\{body}'

    server.sendmail(
        'kalitoosinde@gmail.com',
        msg
        )
    print ('Hey Email has been sent')

    server.quit()


check_price()