import psycopg2
import time

# Generate a list of 10 different user IDs to query
ids = [1000000 + i for i in range(10)]

# Establish a single connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname="performans_test",
    user="postgres",
    password="5530",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Start time measurement
start = time.time()

# Perform queries sequentially (one after another)
for id in ids:
    cur.execute("SELECT * FROM kullanicilar WHERE id = %s", (id,))
    cur.fetchone()  # Fetch the result (not stored or printed)

# End time measurement
end = time.time()

print(f"Total time spent for sequential test: {end - start:.2f} seconds")

# Close the cursor and the database connection
cur.close()
conn.close()
