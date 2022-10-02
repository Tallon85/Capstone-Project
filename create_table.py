import sqlite3

def create_schema(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        phone TEXT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        active INTEGER DEFAULT '1',
        date_created TEXT,
        hire_date TEXT,
        user_type INTEGER DEFAULT '0'
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Competencies(
        competency_id INTEGER PRIMARY KEY AUTOINCREMENT,
        competency_name TEXT,
        date_created TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Assessments(
        assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        assessment_name TEXT,
        competency_id INTEGER,
        date_created TEXT,
        competency_scale TEXT DEFAULT (0-4),
        FOREIGN KEY (competency_id)
            REFERENCES Competencies (competency_id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Assessment_Results(
        assessment_id INTEGER,
        user_id INTEGER,
        assessment_score INTEGER,
        date_taken TEXT,
        FOREIGN KEY (assessment_id)
            REFERENCES Assessments (assessment_id)
        FOREIGN KEY (user_id)
            REFERENCES Users (user_id)
    );
    """)

    connection.commit()

    return True








connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()
result = create_schema(cursor)