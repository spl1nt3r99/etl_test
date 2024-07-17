import datetime
import logging

from helper.helper_postgres import init_logger, create_connection, load_data
from helper.transformation import merge_data

if __name__ == '__main__':
    try:
        start = datetime.datetime.now()

        init_logger()
        engine = create_connection()
        data = merge_data()
        load_data(data, engine)

        end = datetime.datetime.now()
        logging.info(f'Extracting data is completed in {(end - start).total_seconds()}.')
    except Exception as e:
        logging.info('Extracting was failed.')
