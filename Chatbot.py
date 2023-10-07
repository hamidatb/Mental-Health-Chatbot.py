
import random
import json
import datetime

# A list to store the user's mood history.
mood_history = []


def main():
    print("Welcome to the Mental Health Chatbot! We're here to help you feel better 😊")
    while True:
        user_input = input("Type 'mood', 'affirmation', 'activity', 'resources', 'history', or 'quit': ").lower().strip()
      
        # Input your mood and receive a suggestion based on it
        if user_input == "mood":
            mood = input("How are you feeling today? (e.g., happy, sad, stressed, etc.): ").lower().strip()
            track_mood(mood)
            print("Thank you for sharing your mood. Here's a suggestion for you:")
            if mood in ["stressed", "anxious", "sad", "angry"]:
                print("I'm sorry to hear that you're feeling that way. :(")
                print(get_calming_activity())
            else:
                print("That's awesome! Here's another dose of positivity for you: ")
                print(get_positive_affirmation())
        
        # Get a random positive affirmation
        elif user_input == "affirmation":
            print(get_positive_affirmation())
        
        # Get a random calming activity
        elif user_input == "activity":
            print(get_calming_activity())
        
        # Get mental health resources
        elif user_input == "resources":
            print(get_mental_health_resources())
        
        # Check your mood history
        elif user_input == "history":
            print_mood_history()
        
        # Exit the chatbot
        elif user_input == "quit":
            break
        
        # Handle invalid input
        else:
            print("Oops! Invalid input. Please try again 😊") 


# Add a mood entry to mood_history
def track_mood(mood):
    mood_entry = {
        "mood": mood,
        "date": str(datetime.date.today())
    }
    mood_history.append(mood_entry)


# Print the user's mood history
def print_mood_history():
    if not mood_history:
        print("No mood history available. Share your mood to start tracking!")
        return
    print("Your mood history:")
    for entry in mood_history:
        print(f"{entry['date']}: {entry['mood']}")
        
def get_positive_affirmation():
    affirmations = [
        "You are doing great!",
        "You are enough.",
        "You are strong and resilient.",
        "Believe in yourself and your abilities.",
        "You can overcome any challenge."
    ]
    return random.choice(affirmations)
      #This function can definately be evolved in the future to have more input subsections.


def get_calming_activity():
    activities = [
        "Take deep breaths for 5 minutes.",
        "Practice mindfulness meditation.",
        "Take a walk in nature.",
        "Listen to calming music.",
        "Do some stretching or yoga."
    ]
    return random.choice(activities)


def get_mental_health_resources():
    resources = {
        "Crisis Text Line Canada": "Text CONNECT to 686868",
        "Canada Suicide Prevention Service": "1-833-456-4566",
        "Canadian Mental Health Association": "Find local support at https://www.cmha.ca/get-involved/find-your-cmha",
    }
    return json.dumps(resources, indent=2)

if __name__ == "__main__":
    main()
    
    
