import json
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

# חיבור למסד הנתונים
client = MongoClient('mongodb+srv://shlomit5452:shk1234@cluster0.faecgrb.mongodb.net/?retryWrites=true&w=majority')
db = client['myDatabase']  # שינוי שם ה-Database שלך

# יצירת Collection למשתמשים
users_collection = db['users']

# יצירת Collection ל-UserDB
user_db_collection = db['UserDB']

# קריאת נתוני המשתמשים מה-JSON
with open('C:\\dell\\full stack\\Full Stack Final Project\\server\\Users.json') as users_file:
    users_data = json.load(users_file)

# יצירת ObjectId חדש
user_id = ObjectId()

# הוספת המשתמש 'admin' עם הסיסמה 'admin_password' למסד הנתונים
admin_user = {
    '_id': user_id,
    'UserName': 'admin',
    'Password': 'admin_password'
}

# הוספת המשתמש 'admin' לקולקציה 'users'
users_collection.insert_one(admin_user)
print(f"Added admin user with ID: {user_id}")

# הוספת המשתמש 'admin' לקולקציה של UserDB רק עם UserName ו־Password
admin_user_db = {
    'UserName': 'admin',
    'Password': 'admin_password'
}

user_db_collection.insert_one(admin_user_db)
print("Added admin user to UserDB")

# הוספת הרשאות למשתמש 'admin'
permissions_collection = db['permissions']
with open('C:\\dell\\full stack\\Full Stack Final Project\\server\\Permissions.json') as permissions_file:
    permissions_data = json.load(permissions_file)

for permission in permissions_data:
    permissions_collection.insert_one(permission)
print("Added admin permissions")

print("Users and permissions added successfully!")