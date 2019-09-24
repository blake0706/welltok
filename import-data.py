import csv
import psycopg2

conn = psycopg2.connect("host=localhost port=5432 dbname=test user=postgres")
cur = conn.cursor()
with open('import.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader) # Skip the header row.
    for row in reader:
        if len(row) != 0:
            cur.execute(
                "INSERT INTO topics_topic(topic_id, title, description, author, tags, created_at, updated_at) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                row
        )
conn.commit()
