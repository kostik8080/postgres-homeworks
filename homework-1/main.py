"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import csv



with psycopg2.connect(host='localhost', database='north', user='postgres', password='12345') as conn:
    with conn.cursor() as cur:
        with open("north_data\\employees_data.csv", "r", newline="") as file:
            atribute = csv.DictReader(file)

            for attr in atribute:

                cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                        (int(attr["employee_id"]), attr["first_name"], attr["last_name"], attr["title"], attr["birth_date"], attr["notes"]))


    with conn.cursor() as cur:
        with open("north_data\\customers_data.csv", "r", newline="") as file:
            atribute = csv.DictReader(file)

            for attr in atribute:

                cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                        (attr["customer_id"], attr["company_name"], attr["contact_name"]))


    with conn.cursor() as cur:
        with open("north_data\\orders_data.csv", "r", newline="") as file:
            atribute = csv.DictReader(file)

            for attr in atribute:

                cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                        (int(attr["order_id"]), attr["customer_id"], int(attr["employee_id"]), attr["order_date"], attr["ship_city"]))


conn.close()

