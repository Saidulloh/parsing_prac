# import requests
# from bs4 import BeautifulSoup as BS
# import csv

# header = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
# }

# for i in range(1,10):
#     url = f'https://shop.casio.ru/catalog/?PAGEN_1={i}'  

#     req = requests.get(url, headers=header)

#     src = req.text

#     soup = BS(src, 'lxml')
#     text = soup.find_all(class_='product-item__articul')
#     prise = soup.find_all(class_='product-item__price')
#     href = soup.find_all('a',class_='product-item__link')
#     informarions = []

#     for i in range(len(text)):
#         link = href[i].get('href')
#         all_info = f'{prise[i].text.split()[1]} {prise[i].text.split()[2]} {prise[i].text.split()[0]}'
#         name = text[i].text
#         links = f'https://shop.casio.ru/{link}'

#         with open('lesson_22/prac/clocks.csv', 'a', encoding='utf-8') as file:
#             wr = csv.writer(file)
#             wr.writerow((name.strip() + ' - ' + all_info, '\n' + links + '\n'))