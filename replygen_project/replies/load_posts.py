import pandas as pd
from pymongo import MongoClient
import datetime

client = MongoClient("mongodb+srv://mohitpads2005:4PvrtIL5KAMfoOBi@cluster0.tmza8j0.mongodb.net/")

db = client['replygen_db']
posts_col = db['posts']

df = pd.read_excel(r"D:\Technical Interview\posts.xlsx")


for _, row in df.iterrows():
    posts_col.insert_one({
        "platform": row['platform'],
        "post_text": row['post_text'],
        "timestamp": datetime.datetime.now(datetime.UTC)
    })

print("Posts loaded successfully.")
