import sqlite3
import bcrypt
import manager_view
import user_view

connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()
email=input("Enter User email: ")
elist=[]
sql_find_email=("SELECT email FROM Users WHERE active=1")
rows= cursor.execute(sql_find_email,).fetchall()
for row in rows:
    elist.append(row[0])
while True:
    # salt = bcrypt.gensalt()
    if email in elist:
        user_password=input("Enter password: ")
        values=(email,)
        sql_find_email=("SELECT password FROM Users WHERE email=?")
        row= cursor.execute(sql_find_email,values).fetchone()
        # user_password = input("Type in a password: ")
        # password_salt = bcrypt.gensalt()

        recieve = bcrypt.checkpw(user_password.encode("utf-8"),row[0].encode())

        print()

        # recieve = hashed_password.decode()

        # print(recieve)

       

        # recieve = bcrypt.checkpw(user_password.encode(),decoded_password.encode())

        # recieve=bcrypt.hashpw(password.encode("utf-8"),salt)
        if recieve:
            sql_find_email=("SELECT user_type FROM Users WHERE email=?")
            row= cursor.execute(sql_find_email,values).fetchone() 
            manager=row[0]
            if manager== 1:
                manager_view.view_all()
                break
            elif manager== 0:
                value=(email,)
                sql_find_user_id=("SELECT user_id FROM Users WHERE email=?")
                row= cursor.execute(sql_find_user_id,value).fetchone()
                user_id=row[0]
                user_view(user_id)
                while True:
                    print("*** User Menu ***")
                    action = str(input("[1] View Competenciess\n[2] View Assessment Results\n[3] Edit User Data\nPress 'ENTER to return to login\n"))
                    if action == "1":
                        rows = cursor.execute("SELECT * FROM Competencies")
                        print(f"{'Competencies'}")
                        print("----------------------")
                        for row in rows:
                            print(f"{row[0]}")

                    if action == "2":
                        rows = cursor.execute(f"SELECT assessment_id, assessment_score, date_taken FROM Assessment_Results WHERE user_id = '{user_id}'")
                        print(f"{'Assessment Id'} {'Score':<10} {'Date Taken'}")
                        print("---------------------------------------------------")
                        for row in rows:
                            print(f"{row[0]} {row[1]:<10} {row[2]}")

                    if action == "3":
                        while True:
                            user_input = str(input("[1] Edit First Name\n[2] Edit Last Name\n[3] Edit Phone Number\n[4] Edit Email\n[5] Edit Password\n[6] User Active\n [7] User Type\n Press 'ENTER to return to Manager Edit Menu\n"))

                            if user_input == "1":
                                update_fname = input("Enter New First Name: ")
                                cursor.execute(f"UPDATE Users SET first_name = '{update_fname}' WHERE user_id = '{user_id}'")
                                print("Success: First Name was updated!")
                                connection.commit()
                            elif user_input == "2":
                                update_lname = input("Enter New Last Name: ")
                                cursor.execute(f"UPDATE Users SET last_name = '{update_lname}' WHERE user_id = '{user_id}'")
                                print("Success: Last Name was updated!")
                                connection.commit()
                            elif user_input == "3":
                                update_phone = input("Enter New Phone Number: ")
                                cursor.execute(f"UPDATE Users SET phone = '{update_phone}' WHERE user_id = '{user_id}'")
                                print("Success: Phone Number was updated!")
                                connection.commit()
                            elif user_input == "4":
                                update_email = input("Enter New Email: ")
                                cursor.execute(f"UPDATE Users SET email = '{update_email}' WHERE user_id = '{user_id}'")
                                print("Success: Email was updated!")
                                connection.commit()
                            elif user_input == "5":
                                update_pass = input("Enter New Password: ")
                                bytes = update_pass.encode('utf-8')
                                # generating the salt
                                salt = bcrypt.gensalt()
                                # Hashing the password
                                hash = bcrypt.hashpw(bytes, salt)
                                cursor.execute(f"UPDATE Users SET password = '{hash.decode}' WHERE user_id = '{user_id}'")
                                print("Success: Password was updated!")
                                connection.commit()
                    if action =="":

    
                        break
            else:
                print("It appears there is a technical issue. Please contact you IT cordinator")
        else:
            print("Invalid Password Try again")
    else:
        print("\ntry again\n")

connection.commit
    
