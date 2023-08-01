import pandas as pd
import requests
from bs4 import BeautifulSoup
import re


def get_book_info(row):
    title = row['도서명']
    author = row['저자']
    pub = row['출판사']
    year = row['발행년도']
    url = 'http://www.yes24.com/Product/Search?domain=BOOK&query={}'

    r = requests.get(url.format(row['ISBN']))
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        if pd.isna(title):
            title = soup.find('a', attrs={'class': 'gd_name'}) \
                .get_text()
    except AttributeError:
        pass

    try:
        if pd.isna(author):
            authors = soup.find('span', attrs={'class': 'info_auth'}) \
                .find_all('a')
            author_list = [auth.get_text() for auth in authors]
            author = ','.join(author_list)
    except AttributeError:
        pass

    try:
        if pd.isna(pub):
            pub = soup.find('span', attrs={'class': 'info_pub'}) \
                .find('a') \
                .get_text()
    except AttributeError:
        pass

    try:
        if year == -1:
            year_str = soup.find('span', attrs={'class': 'info_date'}) \
                .get_text()
            year = re.findall(r'\d{4}', year_str)[0]
    except AttributeError:
        pass

    return title, author, pub, year

def data_fixing(ns_book4):
    ns_book4 = ns_book4.astype({'도서권수': 'int32', '대출건수': 'int32'})

    set_isbn_na_rows = ns_book4['세트 ISBN'].isna()
    ns_book4.loc[set_isbn_na_rows, '세트 ISBN'] = ''

    ns_book5 = ns_book4.replace({'발행년도': '.*(\d{4}).*'}, r'\1', regex=True)
    unkown_year = ns_book5['발행년도'].str.contains('\D', na=True)
    ns_book5.loc[unkown_year, '발행년도'] = '-1'

    ns_book5 = ns_book5.astype({'발행년도': 'int32'})
    dangun_yy_rows = ns_book5['발행년도'].gt(4000)
    ns_book5.loc[dangun_yy_rows, '발행년도'] = ns_book5.loc[dangun_yy_rows, '발행년도'] - 2333
    dangun_year = ns_book5['발행년도'].gt(4000)
    ns_book5.loc[dangun_year, '발행년도'] = -1
    old_books = ns_book5['발행년도'].gt(0) & ns_book5['발행년도'].lt(1900)
    ns_book5.loc[old_books, '발행년도'] = -1

    na_rows = ns_book5['도서명'].isna() | ns_book5['저자'].isna() \
              | ns_book5['출판사'].isna() | ns_book5['발행년도'].eq(-1)
    updated_sample = ns_book5[na_rows].apply(get_book_info,
                                             axis=1, result_type='expand')

    ns_book6 = ns_book5.dropna(subset=['도서명', '저자', '출판사'])
    ns_book6 = ns_book6[ns_book6['발행년도'] != -1]

    return ns_book6

if __name__ == '__main__':
    ns_df = pd.read_csv('ns_202104.csv', low_memory=False)
    ns_book = ns_df.dropna(axis=1, how='all')
    count_df = ns_book[['도서명', '저자', 'ISBN', '권', '대출건수']]
    loan_count = count_df.groupby(by=['도서명', '저자', 'ISBN', '권'], dropna=False).sum()
    dup_rows = ns_book.duplicated(subset=['도서명', '저자', 'ISBN', '권'])
    unique_rows = ~dup_rows
    ns_book3 = ns_book[unique_rows].copy()
    ns_book3.set_index(['도서명', '저자', 'ISBN', '권'], inplace=True)
    ns_book3.update(loan_count)
    ns_book4 = ns_book3.reset_index()
    ns_book4 = ns_book4[ns_book.columns]

    print(data_fixing(ns_book4))