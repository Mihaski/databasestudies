"""Скрипт для заполнения данными таблиц в БД Postgres."""

import csv

import psycopg2


def get_data_from_csv(tablename, filename):
    conn = psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password="12345678",
    )
    cursor = conn.cursor()

    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)
        for row in csv_reader:
            query = f"INSERT INTO {tablename} ({', '.join(header)}) VALUES ({', '.join(['%s'] * len(row))})"
            cursor.execute(query, row)

    conn.commit()
    cursor.close()
    conn.close()


def main():
    get_data_from_csv("customers", "north_data/customers_data.csv")
    get_data_from_csv("orders", "north_data/orders_data.csv")
    get_data_from_csv("employees", "north_data/employees_data.csv")


if __name__ == "__main__":
    main()
