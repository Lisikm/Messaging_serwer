from create_db import db_creation, db_tables_creation

print("Welcome in Messaging Serwer!\nLet's start with creating a database.")
db_created = False
while not db_created:
    db_name = input("Enter database name: ")
    db_created = db_creation(db_name)
    if not db_created:
        print("DB creation failed. There is already a database with the given name. Try again.")
    else:
        print(f"Congratulations! DB '{db_name}' created!")
db_tables_creation(db_name)

