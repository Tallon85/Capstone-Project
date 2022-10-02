def export_all():
    import sqlite3
    import csv
    connection = sqlite3.connect('capstone.db')
    cursor = connection.cursor()

    while True:
        print("CSV Export/Import")
        user_input = str(input("[1] Export User List\n[2] Export Competencies List\n[3] Import Assessment Results\n"))

        if user_input == "1":
            fields = ['User ID' , 'First Name' , 'Last Name' , 'Phone' , 'Email' , 'Password', 'Active', 'Date Created', 'Hire Date', 'User Type']
            data = cursor.execute("SELECT * FROM Users")
            with open('export_users.csv', 'w',newline="",encoding='utf-8') as csvfile:
        
                writer = csv.writer(csvfile)

                writer.writerow(fields)
                writer.writerows(data)

        if user_input =="2":
            fields = ['Competency ID', 'Competency Name', 'Date Created']
            data = cursor.execute("Select * FROM Competencies")
            with open('export_competencies.csv', 'w', newline="",encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)

                writer.writerow(fields)
                writer.writerows(data)

        if user_input == "3":
            with open("assessment.csv","r") as infile:
                
                values=infile.readlines()[1::]
                for value in values:
                    value=value.strip().split(",")
                    sql_import="INSERT INTO Assessment_Results(assessment_id,user_id,assessment_score,date_taken) VALUES(?,?,?,?)"
                    print(value)
                    cursor.execute(sql_import,value)
                connection.commit()



