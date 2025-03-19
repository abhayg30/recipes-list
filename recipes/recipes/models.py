from django.conf import settings
from pymongo import MongoClient

mongo_client = MongoClient(settings.MONGO_URI)
recipes_db = mongo_client["recipes_db"]
recipes_collection = recipes_db["recipes"]
