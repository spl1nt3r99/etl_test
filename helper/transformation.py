import logging

import pandas
import pandas as pd


def merge_data():
    logging.info('Merging JSON and CSV data...')
    try:
        json = get_json_data('large_products_data.json')
        csv = get_csv_data('large_sales_data.csv')
        merged = pd.merge(csv, json, on='product_id', how='inner', validate='m:1')
        merged.drop_duplicates(inplace=True)

        logging.info('JSON and CSV data successfully merged.')
        return merged
    except Exception as e:
        logging.error(e)


def get_json_data(file_name):
    logging.info('Extracting JSON data...')
    try:
        data = pd.read_json(f'raw_data/{file_name}')
        data.rename(columns={'price': 'product_price'}, inplace=True)

        # Filter out invalid categories
        data['product_name'] = data['product_name'].str.upper()
        data['product_name'] = data['product_name'].replace('PRODUCT', 'Product', regex=True)
        valid_product_name = data['product_name'].str.contains(r'^Product [A-Z]$')
        data = data[valid_product_name]
        data.drop_duplicates(inplace=True)

        logging.info(f'Total JSON elements are {len(data)}.')
        return data
    except Exception as e:
        logging.error(e)


def get_csv_data(file_name):
    logging.info('Extracting CSV data...')
    try:
        data = pd.read_csv(f'raw_data/{file_name}')
        data.rename(columns={'price': 'sales_price'}, inplace=True)
        data['sale_date'] = pandas.to_datetime(data['sale_date'])
        data.drop_duplicates(inplace=True)

        logging.info(f'Total CSV elements are {len(data)}.')
        return data
    except Exception as e:
        logging.error(e)
