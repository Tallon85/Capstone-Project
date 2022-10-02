def view_all():
    import sqlite3
    import add_db
    import edit_db
    import export_csv
    connection = sqlite3.connect('capstone.db')
    cursor = connection.cursor()

    while True:
        print("--- Manager Menu ---")
        action = str(input("[1] View Users, Search for users, Report of Users competency, Specific User Competency, List of assessements\n[2] Add a user, New Competency, New Assessment, Assessment Result\n[3] Edit User, Competency, Assessment, Assessment Result, Delete assessment result\n[4] Export/Import CSV\n"))

        if action == '1':
            while True:
                print("### View/Search Menu ###")
                user_input = str(input("[1] View Users\n[2] Search For a User\n[3] View Users Competency\n[4] View Competency Level Of User\n[5] View User Assessments\nPress 'ENTER' to return to manager menu\n"))
                if user_input == '1':
                    rows = cursor.execute("SELECT user_id, first_name, last_name FROM Users")
                    print(f"{'User ID'} {'First Name':<10} {'Last Name'}")
                    print("-------------------------------------------------")
                    for row in rows:
                        print(f"{row[0]} {row[1]:<10} {row[2]}")
                
                if user_input == '2':
                    user_name = input("Enter User you want to search for: ")
                    rows = cursor.execute(f"SELECT user_id, first_name, last_name FROM Users WHERE first_name LIKE'%{user_name}%' OR last_name LIKE'%{user_name}%'")
                    print(f"{'User ID'} {'First Name':<10} {'Last Name'}")
                    print("-------------------------------------------------")
                    for row in rows:
                        print(f"{row[0]} {row[1]:<10} {row[2]}")

                if user_input == '3':
                    rows = cursor.execute("SELECT user_id, assessment_id, assessment_score FROM Assessment_Results")
                    print(f"{'User ID'} {'Assessment ID'} {'Score'}")
                    print("------------------------------------")
                    for row in rows:
                       print(f"{row[0]} {row[1]} {row[2]}")

                if user_input =='4':
                    rows = cursor.execute("SELECT user_id, first_name, last_name FROM Users")
                    print(f"{'User ID'} {'First Name':<10} {'Last Name'}")
                    print("-------------------------------------------------")
                    for row in rows:
                        print(f"{row[0]} {row[1]:<10} {row[2]}")
                    user_id = input("Enter a User Id to view user competency: ")
                    rows2 = cursor.execute(f"SELECT user_id, assessment_id, assessment_score FROM Assessment_Results WHERE user_id = '{user_id}'").fetchall()
                    print(f"{'User ID'} {'Assessment ID'} {'Score'}")
                    print("-------------------------------------")
                    for row in rows2:
                       print(f"{row[0]} {row[1]} {row[2]}")

                if user_input == '5':
                    rows = cursor.execute("SELECT user_id, first_name, last_name FROM Users")
                    print(f"{'User ID'} {'First Name':<10} {'Last Name'}")
                    print("-------------------------------------------------")
                    for row in rows:
                        print(f"{row[0]} {row[1]:<10} {row[2]}")
                    user_id = input("Enter a User ID to view their assessments: ")
                    rows2 = cursor.execute(f"SELECT user_id, assessment_id FROM Assessment_Results WHERE user_id = '{user_id}'").fetchall()
                    print(f"{'User ID'} {'Assessment ID'}")
                    print("-------------------------------------")
                    for row in rows2:
                       print(f"{row[0]} {row[1]}")

                if user_input == '':
                    break

        
        if action == '2':
            add_db.add_things()

        if action == "3":
            edit_db.edit_things()

        if action == "4":
            export_csv.export_all()

