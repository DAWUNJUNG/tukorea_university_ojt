import pandas as pd

def data_cleaning(filename):
    ns_df = pd.read_csv(filename, low_memory=False)
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

    return ns_book4

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

    new_ns_book4 = data_cleaning('ns_202104.csv')
    print(ns_book4.equals(new_ns_book4))