import requests
import smtplib
from bs4 import BeautifulSoup

email = "venkatesanpoova@gmail.com"
password = "lbjroxgzlfqanndq"
url = input("Enter the url of the product: ")
target_price = int(input("Enter the target price: "))
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, 'html.parser')
price = soup.find('span', 'a-price-whole')
og_price = price.text.replace('.', '').replace(',', '')
title = soup.find('span', 'product-title-word-break')
product_title = (title.text).strip()

if int(og_price) < target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(from_addr=email, to_addrs=email,
                            msg=f"Subject:Tracker Alert\n\n Your product{product_title} is lower than your target price")
