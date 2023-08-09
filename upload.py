from pymongo import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd

json_file_path = "data.json"

# Load JSON file into a Pandas DataFrame
df = pd.read_json(json_file_path)

uri = "mongodb+srv://dev:dev1234@cluster0.dcykn42.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Extract database and collection names from the URI
db_name = "Cluster0"
collection_name = "dev"

# Access the specified database and collection
db = client[db_name]
collection = db[collection_name]

# Convert DataFrame to a list of dictionaries
data_dicts = df.to_dict(orient='records')

# Insert the list of documents into the collection
collection.insert_many(data_dicts)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
