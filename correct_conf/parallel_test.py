import psycopg2
import time
from concurrent.futures import ThreadPoolExecutor

# Generate 10 different user IDs to query
ids = [1000000 + i for i in range(10)]

# Define the function that fetches a user by ID from the database
def fetch_user(id):
    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        dbname="performans_test",
        user="postgres",
        password="5530",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    # Execute the SELECT query for the given user ID
    cur.execute("SELECT * FROM kullanicilar WHERE id = %s", (id,))
    cur.fetchone()  # Fetch the result (but do not print/store)

    # Close the cursor and connection
    cur.close()
    conn.close()

# Start time measurement
start = time.time()

# Use ThreadPoolExecutor to run queries in parallel (10 threads)
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(fetch_user, ids)

# End time measurement
end = time.time()
print(f"Total time spent for parallel test: {end - start:.2f} seconds")
