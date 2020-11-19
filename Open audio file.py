import pandas as pd
import numpy as np


def num_never_checked_out():
    lib_books = pd.read_csv(
        "https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-analytics-bootcamp/library-books.csv")
    lib_transactions = pd.read_csv(
        'https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-analytics-bootcamp/library-transactions.csv')
    lib_transactions['checkout_date'].dropna()
    lib_uniquebooks = np.unique(lib_transactions['book_id'])
    filters = lib_books['book_id'].isin(lib_uniquebooks)
    return sum(~filters)


# return the oposit of isin function from pandas ~
# measure the number of books

print(num_never_checked_out())

