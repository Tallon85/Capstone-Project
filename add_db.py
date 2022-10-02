
def add_things():
    import bcrypt
    import sqlite3
    connection = sqlite3.connect('capstone.db')
    cursor = connection.cursor()

    while True:
        print("+++ Manager Add Menu +++")
        action = str(input("[1] Add User\n[2] Add New Competency\n[3] Add New Assessment\n[4] Add Assessment Result\nPress 'ENTER' to return to Manager Menu\n"))

        if action == '1':
            print("**** New User ****")
            print("Please fill out the form below to add a new User:")
            insert_info = "INSERT INTO Users (first_name, last_name, phone, email, password, date_created, hire_date, user_type) VALUES (?,?,?,?,?,?,?,?)"
            while True:
                f_name = input("Enter First Name: ")
                l_name = input("Enter Last Name: ")
                phone = input("Enter Phone Number: ")
                email = input("Enter Email: ")
                password = str(input("Enter Password: "))
                # converting password to array of bytes
                bytes = password.encode('utf-8')
                
                # generating the salt
                salt = bcrypt.gensalt()
                
                # Hashing the password
                hash = bcrypt.hashpw(bytes, salt)
                date = input("Enter Todays Date: ")
                hire = input("Enter The Hire Date: ")
                user_type = input("Enter 1 for Manager or 0 for normal user: ")

                values = (f_name, l_name, phone, email, hash.decode(), date, hire, user_type)
                cursor.execute(insert_info, values)
                print("Success: User was successfully added!")
                connection.commit()
                break

        if action == '2':
            print("**** New Competency ****")
            print("Please fill out the form below to add a new Competency:")
            insert_info = "INSERT INTO Competencies (competency_name, date_created) VALUES (?,?)"
            while True:
                c_name = input("Enter Competency Name: ")
                d_created = input("Enter Todays Date: ")

                values = (c_name, d_created)
                cursor.execute(insert_info, values)
                print("Success: Competency was successfully added!")
                connection.commit()
                break

        if action == '3':
            print("**** New Assessment ****")
            print("Please fill outh the form below to add a new Assessment:")
            insert_info = "INSERT INTO Assessments (assessment_name, competency_id, date_created) VALUES (?,?,?)"
            while True:
                a_name = input("Enter Assessment Name: ")
                c_id = input("Enter Competency ID of Competency you want to add too: ")
                d_create = input("Enter Todays Date: ")

                values = (a_name, c_id, d_create)
                cursor.execute(insert_info, values)
                print("Success: Assessment was successfully added!")
                connection.commit()
                break

        if action == '4':
            print("**** New Assessment Result ****")
            print("Please fill outh the form below to add a new Assessment Result:")
            insert_info = "INSERT INTO Assessment_Results (assessment_id, user_id, assessment_score) VALUES (?,?,?)"
            while True:
                a_id = input("Enter Assessment ID: ")
                u_id = input("Enter User ID: ")
                a_score = input("Enter score for the Assessment: ")
                
                values = (a_id, u_id, a_score)
                cursor.execute(insert_info, values)
                print("Success: Assessment Result was successfully added!")
                connection.commit()
                break

        if action == '':
            break

    