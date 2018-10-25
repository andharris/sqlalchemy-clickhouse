import os
from sqlalchemy import create_engine


def main():
    config = {
        'username': os.getenv('CLICKHOUSE_USERNAME'),
        'password': os.getenv('CLICKHOUSE_PASSWORD'),
        'server': os.getenv('CLICKHOUSE_HOSTNAME'),
        'database': os.getenv('CLICKHOUSE_DATABASE'),
        'port': 8124
    }
    connection_string = 'clickhouse://{username}:{password}@{server}:{port}/{database}'
    connection_string = connection_string.format(**config)
    eng = create_engine(connection_string, connect_args={'https': True})
    print(eng.execute('SELECT count() FROM gis_exceptions_v1 FINAL').scalar())


if __name__ == '__main__':
    main()
