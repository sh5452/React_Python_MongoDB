import json
from pymongo import MongoClient
from bson.objectid import ObjectId

# התחברות למסד הנתונים
client = MongoClient('mongodb://localhost:27017/')
db = client['UserDB']  # שנה לשם ה-Database שלך

# קריאת נתוני המשתמשים מה-JSON
with open('Users.json') as users_file:
    users = json.load(users_file)

with open('Permissions.json') as permissions_file:
    permissions = json.load(permissions_file)

# הוספת המשתמשים למסד הנתונים
for user in users:
    user_id = ObjectId()  # יצירת ObjectId חדש
    user['_id'] = user_id
    db['users'].insert_one({
        '_id': user_id,
        'UserName': 'admin',  # שם משתמש של המנהל מערכת
        'Password': 'admin'   # סיסמה של המנהל מערכת
    })

    # עדכון ה-Id עם ה-ObjectId שנוצר
    user['Id'] = str(user_id)

    # הוספת המשתמש למסד הנתונים
    db['users'].insert_one(user)  # שם ה-Collection של המשתמשים

# הוספת ההרשאות למסד הנתונים
for perm in permissions:
    perm_id = ObjectId()
    perm['_id'] = perm_id
    db['permissions'].insert_one(perm)  # שם ה-Collection של ההרשאות

    # עדכון ה-Id עם ה-ObjectId שנוצר
    perm['Id'] = str(perm_id)

    # הוספת ההרשאות למסד הנתונים
    db['permissions'].insert_one(perm)  # שם ה-Collection של ההרשאות

print("Admin user and permissions added successfully!")