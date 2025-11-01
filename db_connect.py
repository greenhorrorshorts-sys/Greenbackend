from pymongo import MongoClient

uri = "mongodb://greenshorts_db_user:dnpPHkntI0P7KHDy@ac-0.greenshorts.jzq6ip.mongodb.net:27017,ac-1.greenshorts.jzq6ip.mongodb.net:27017,ac-2.greenshorts.jzq6ip.mongodb.net:27017/?ssl=true&replicaSet=atlas-xxxx-shard-0&authSource=admin&retryWrites=true&w=majority"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("✅ Successfully connected to MongoDB!")
except Exception as e:
    print("❌ Connection failed:", e)

