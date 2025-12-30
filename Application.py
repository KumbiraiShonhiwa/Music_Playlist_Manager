from Database import *

def main ():
    db = Database()
    db.load_test_data()
    user = db.authenticate()
    db.run_menu(user)
 #  db.export_data()
    
if __name__ == "__main__":
    main()