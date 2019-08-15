# coding: UTF-8
import csv
import urllib3
import certifi
from bs4 import BeautifulSoup

import time

for i in range(1, 15, 1):
    time.sleep(3)
    print('page : ', i)
    target_url = 'https://icws.indigo-bell.com/search?page=' + str(i) + '&q=%E3%81%AB%E3%81%AA&st=n'
    # httpsの証明書検証を実行している
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())

    r = http.request('GET', target_url)

    soup = BeautifulSoup(r.data, 'html.parser')

    tbody = soup.findAll('tbody')[0]
    rows = tbody.findAll("tr")

    with open("imas_cg_nina.txt", "a", encoding='shift-jis') as f:
        writer = csv.writer(f)
        for row in rows:
            csv_row = []
            for cell in row.findAll('td')[3]:
                csv_row.append(cell)
            writer.writerow(csv_row)
