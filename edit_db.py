
def edit_things():
    import sqlite3
    connection = sqlite3.connect('capstone.db')
    cursor = connection.cursor()

    while True:
        print("#### Manager Edit Menu ####")
        action = str(input("[1] Edit User\n[2] Edit Competency\n[3] Edit Assessment\n[4] Edit Assessment Result\n[5] Delete Assessment Result\nPress 'ENTER' to return to manager menu\n"))

        if action == "1":
            while True:
                print("*** Edit User ***")
                user_choice = input("Enter user id of User you want to Edit: ")
                user_input = str(input("[1] Edit First Name\n[2] Edit Last Name\n[3] Edit Phone Number\n[4] Edit Email\n[5] Edit Password\n[6] User Active\n [7] User Type\n Press 'ENTER to return to Manager Edit Menu\n"))

                if user_input == "1":
                    update_fname = input("Enter New First Name: ")
                    cursor.execute(f"UPDATE Users SET first_name = '{update_fname}' WHERE user_id = '{user_choice}'")
                    print("Success: First Name was updated!")
                    connection.commit()
                elif user_input == "2":
                    update_lname = input("Enter New Last Name: ")
                    cursor.execute(f"UPDATE Users SET last_name = '{update_lname}' WHERE user_id = '{user_choice}'")
                    print("Success: Last Name was updated!")
                    connection.commit()
                elif user_input == "3":
                    update_phone = input("Enter New Phone Number: ")
                    cursor.execute(f"UPDATE Users SET phone = '{update_phone}' WHERE user_id = '{user_choice}'")
                    print("Success: Phone Number was updated!")
                    connection.commit()
                elif user_input == "4":
                    update_email = input("Enter New Email: ")
                    cursor.execute(f"UPDATE Users SET email = '{update_email}' WHERE user_id = '{user_choice}'")
                    print("Success: Email was updated!")
                    connection.commit()
                elif user_input == "5":
                    update_pass = input("Enter New Password: ")
                    cursor.execute(f"UPDATE Users SET password = '{update_pass}' WHERE user_id = '{user_choice}'")
                    print("Success: Password was updated!")
                    connection.commit()
                elif user_input == "6":
                    update_active = input("Enter 1 for active or 0 for not active: ")
                    cursor.execute(f"UPDATE Users SET active = '{update_active}' WHERE user_id = '{user_choice}'")
                    print("Succes: User Acitve was epdated!")
                    connection.commit()
                elif user_input == "7":
                    update_type = input("Enter 1 for Manager or 0 for User: ")
                    cursor.execute(f"UPDATE Users SET user_type = '{update_type}' WHERE user_id = '{user_choice}'")
                    print("Success: User Type was updated!")
                    connection.commit()
                elif user_input == "":
                    break

        if action == "2":
            while True:
                print("*** Edit Competency ***")
                user_choice = input("Enter Competency ID of Competency you want to edit:  ")
                update_comp_name = input("Enter New Competency Name: ")
                cursor.execute(f"UPDATE Competencies SET competency_name = '{update_comp_name}' WHERE competency_id = '{user_choice}'")
                print("Success: Competency Name was updated!")
                connection.commit()
                break

        if action =="3":
            while True:
                print("*** Edit Assessment ***")
                user_choice = input ("Enter Assessment ID of Assessment you want to edit: ")
                user_input = str(input("[1] Edit Assessment Name\n[2] Edit Competency ID\nPress 'ENTER' to return to Manager Edit Menu\n"))
                
                if user_input == "1":
                    update_cname = input("Enter New Assessment Name: ")
                    cursor.execute(f"UPDATE Assessments SET assessment_name = '{update_cname}' WHERE assessment_id = '{user_choice}'")
                    print("Success: Assessment Name was updated!")
                    connection.commit()
                elif user_input == "2":
                    update_cid = input("Enter New Competency Id: ")
                    cursor.execute(f"UPDATE Assessments SET competency_id = '{update_cid}' WHERE assessment_id = '{user_choice}'")
                    print("Success: Competency Id was updated!")
                    connection.commit()
                elif user_input == "":
                    break

        if action == "4":
            while True:
                print("*** Edit Assessment Result ***")
                user_choice = input("Enter Assessment ID of Assessment Result you want to edit: ")
                user_input = str(input("[1] Edit User ID\n[2] Edit Assessment Score\n[3] Edit Date Taken\nPress 'ENTER' to return to Manager Edit Menu\n"))

                if user_input == "1":
                    update_uid = input("Enter New User ID: ")
                    cursor.execute(f"UPDATE Assessment_Results SET user_id = '{update_uid}' WHERE assessment_id = '{user_choice}'")
                    print("Success: User Id was updated!")
                    connection.commit()
                elif user_input == "2":
                    update_ascore = input("Enter New Assessment Score: ")
                    cursor.execute(f"UPDATE Assessment_Results SET assessment_score = '{update_ascore}' WHERE assessment_id = '{user_choice}'")
                    print("Success: Assessment Score was updated!")
                    connection.commit()
                elif user_input == "3":
                    update_dtaken = input("Enter New Date: ")
                    cursor.execute(f"Update Assessment_Results SET date_taken = '{update_dtaken}' WHERE assessment_id = '{user_choice}'")
                    print("Success: Date was successfully updated!")
                    connection.commit()
                elif user_input == "":
                    break

        if action == "5":
            print("*** Delete Assessment Result ***")
            user_choice = input("Enter Assessment ID of Assessment Result you want to delete: ")
            user_input = input(f"Are you sure youi want to DELETE Assessment ID #{user_choice} ---- (Y/N)? ")
            if user_input.capitalize() == "Y":
                cursor.execute(f"DELETE FROM Assessment_Results WHERE assessment_id = '{user_choice}'")
                print("Success: Assessment Result was deleted!")
                connection.commit()
            elif user_input.capitalize() == "N":
                break

        if action == "":
            break
