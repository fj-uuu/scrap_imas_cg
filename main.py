# coding: UTF-8
import csv
import urllib3
import certifi
from bs4 import BeautifulSoup
import time

base_url = 'https://icws.indigo-bell.com/search?page='
# idol_page = '&q=%E3%81%AB%E3%81%AA&st=n' # 仁奈ちゃん
idol_page = '&q=高垣&st=n'
out_file = 'imas_cg_kaede.txt'

for i in range(1, 16, 1):
    time.sleep(3)
    print(f'page : {i}')
    target_url = base_url + str(i) + idol_page
    # httpsの証明書検証を実行
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())

    r = http.request('GET', target_url)

    soup = BeautifulSoup(r.data, 'html.parser')

    tbody = soup.findAll('tbody')[0]
    rows = tbody.findAll('tr')

    with open(out_file, 'a', encoding='shift-jis') as f:
        writer = csv.writer(f)
        for row in rows:
            csv_row = []
            for cell in row.findAll('td')[3]:
                csv_row.append(cell)
            writer.writerow(csv_row)
