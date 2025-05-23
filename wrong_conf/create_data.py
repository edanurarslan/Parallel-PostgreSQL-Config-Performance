import psycopg2
from faker import Faker
from datetime import datetime

# Dummy data with faker
fake = Faker()

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="performans_test",
    user="postgres",
    password="1234",  
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Settings for creating data
batch_size = 10000  
total_rows = 10000000  

for i in range(0, total_rows, batch_size):
    records = []
    for _ in range(batch_size):
        records.append((
            fake.first_name(),
            fake.last_name(),
            fake.email(),
            fake.date_of_birth(minimum_age=18, maximum_age=90),
            datetime.now()
        ))

    args_str = b','.join(
        cur.mogrify("(%s, %s, %s, %s, %s)", x) for x in records
    )
    cur.execute(
        b"INSERT INTO kullanicilar (name, surname, eposta, dogum_tarihi, olusturma_zamani) VALUES " + args_str
    )
    conn.commit()
    print(f"{i + batch_size} records inserted...")

cur.close()
conn.close()
print("All data created successfully.")

