import logging

import psycopg2
from sqlalchemy import create_engine


def init_logger():
    logging.basicConfig(level=logging.INFO, format=' %(asctime)s :: %(name)s :: %(levelname)-8s :: %(message)s')
    logging.info('Python test etl project is started.')


def create_connection():
    logging.info('Connecting to the PostgreSQL...')
    try:
        return create_engine('postgresql+psycopg2://postgres:pass@localhost/etl_test')
    except psycopg2.DatabaseError as error:
        logging.error(error)


def load_data(data, engine):
    logging.info("Load data...")

    try:
        data.to_sql(name='product_sales', con=engine, if_exists='replace', index=False)
    except Exception as e:
        logging.error(e)

    logging.info("Data loading is complete.")
