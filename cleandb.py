from pymongo import MongoClient
import sys
import pprint

mongo_server = "localhost:27017"

client = MongoClient(mongo_server, serverSelectionTimeoutMS=200, unicode_decode_error_handler='ignore')

db = client["pcap"]

db["pcap"].drop()

print("Packets deleted")