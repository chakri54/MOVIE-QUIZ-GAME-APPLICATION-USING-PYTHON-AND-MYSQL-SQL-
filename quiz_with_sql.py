import random
import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',          # Change this if your MySQL server is hosted elsewhere
    user='your_username',      # Your MySQL username
    password='your_password',   # Your MySQL password
    database='quiz_game'       # Your database name
)

cursor = conn.cursor()

print('*' * 26)
print('*' * 10, "QUIZ", '*' * 10)
print('*' * 26)

user_count = 0
all_score = {}
all_gifts = {}
add_cash = {}

while True:
    user_count += 1
    Name = input("Enter Your Name: ").upper()

    # Define questions (same as before)
    questions = {
        # (Your questions go here...)
    }
    
    score = 0
    qno = 1
    score_report = {}
    report = {}

    for q in questions:
        print(q)
        valid_options = ['a', 'b', 'c', 'd']
        while True:
            ch = input("Choose an option: ").lower()
            if ch in valid_options:
                if ch == questions[q]:
                    print("Correct")
                    score += 1
                    score_report[qno] = 1
                    report[qno] = "Correct"
                else:
                    print("Incorrect")
                    score -= 0.5
                    score_report[qno] = 0.5
                    report[qno] = "Incorrect"
                break
            else:
                print("Enter a valid option (a, b, c, or d)")
                
        qno += 1

    print()
    print()
    wrong_count = 0
    correct_count = 0
    for i in report.keys():
        print(i, ' ' * 20, ":" * 5, report[i], ":" * 5, ' ' * 20, score_report[i])
        if report[i] == "Incorrect":
            wrong_count += 1
        elif report[i] == "Correct":
            correct_count += 1

    print()
    print(f"TOTAL CORRECT: {correct_count}   TOTAL INCORRECT: {wrong_count}")
    print("Total Points:", score)
    all_score[Name] = score
    print()

    # Handle rewards and gifts
    gift = None
    additional_cash = None

    if score == 15:
        print("You Rocked it!")
        print(f"{Name} You won CASH Prize:", score * 100)
        gift_items = ["Smart Watch", "OTT subscription", "Headset", "Additional Cash Back"]
        gift = random.choice(gift_items)
        if gift == gift_items[3]:
            additional_cash = 1000
            print("You Have Received Additional Cash Back of ₹:", additional_cash)
        # ... (Handle other gifts)

    # (Handle other score ranges...)

    # Store the results in the database
    cursor.execute('''
    INSERT INTO quiz_results (name, score, gift, additional_cash) 
    VALUES (%s, %s, %s, %s)
    ''', (Name, score, gift, additional_cash))

    conn.commit()  # Commit changes to the database

    print()
    ch = input("Do you want to play the quiz again? Press 'y' or 'n': ")
    if ch == 'n':
        break

# Fetch and display all user data
cursor.execute("SELECT * FROM quiz_results")
rows = cursor.fetchall()

print("REPORT")
print("=" * 50)
print(f"Total Users Played: {user_count}")
print("=" * 50)

for row in rows:
    print("=" * 50)
    print(f"NAME: {row[1]}")
    print(f"Score: {row[2]}")
    print(f"Gift: {row[3] if row[3] else 'None'}")
    print(f"Additional Cashback Rewarded: {row[4] if row[4] else 'None'}")
    print("-" * 50)

print("=" * 50)

# Closing the database connection
cursor.close()
conn.close()
