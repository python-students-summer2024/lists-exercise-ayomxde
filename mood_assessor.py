import os 
import datetime

def get_mood_from_user():
    valid_moods = {
        "happy": 2,
        "relaxed": 1,
        "apathetic": 0,
        "sad": -1
        "angry": -2
    }
    while True:
        mood = input("Please enter your current mood (happy, relaxed, apathetic, sad, angry): ").strip().lower()
        if mood in valid_moods:
            return valid_moods[mood]
        print("Invalid mood. Please try again.")

def mood_already_entered_today(date_today):
    if not os.path.exists('data/mood_diary.txt'):
        return False
    
    with  open('data/mood_diary.txt', 'r') as file:
        lines = file.readlines()
        if lines and lines [-1].startswith(date_today):
            return True
        return False
    
def store_mood(date_today, mood_value):
    if not os.path.exists('data'):
        os.makedirs('data')

    with open('data/mood_diary.txt','a') as file:
        file.write(f"{date_today}, {mood_value}\n")

def diagnose_mood_disorder():
    with open('data/mood_diary.txt', 'r') as file:
        lines = file.readlines()

    if len(lines)<7:
        return
    
    recent_entries = [int(line.strip().split(',')[1]for line in lines[-7:]]
    average_mood = round(sum(recent_entries) / 7)

    if recent_entries.count(2)>=5:
        diagnosis = "manic"
    elif recent_entries.count(-1)>=4:
        diagnosis = "depressive"
    elif recent_entries count(0)>+ 6:
        diagnosis = "schizoid"
    else:
        mood_names = {2: "happy", 1: "relaxed", 0:"apathetic", -1: "sad", -2: "angry"}
        diagnosis = mood_names.get(average_mood, "unknown")
    
    print(f"Your diagnosis: {diagnosis}!")

def assess_mood():
    date_today = str(datetime.date.today())
    
    if mood_already_entered_today(date_today):
        print("Sorry, you have already entered your mood today.")
        return
    
    mood_value = get_mood_from_user()
    store_mood(date_today, mood_value)
    diagnose_mood_disorder()
