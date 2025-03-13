import json
import random
from datetime import datetime, timedelta

generated_events = 0
genreated_users = 0

# Generate user data
def generate_user(user_id):
    """
    Funcion to generate a user with the features:
        - user_id: int
        - age: int
        - location: str
        - subscription_status: str
    """
    return {
        "user_id": user_id,
        "age": random.randint(18, 65),
        "location": random.choice(["USA", "Canada", "UK", "Germany", "India", "Australia"]),
        "subscription_status": random.choice(["free", "premium", "trial"])
    }

def generate_event(event_id, user_id, add_event_interval, start_date):
    """
    Function to generate an event with the following data:
        - event_time: timestamp
        - event_id: int
        - user_id: int
        - click_count: int
        - time_spent: float
        - scroll_depth: float
        - purchase_completed: int  
        - checkout_time: timestamp
        - ad_interaction: int
        - session_duration: float
        - bounce_rate: float
    """
    base_data = {
                "event_time":  datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S") + timedelta(hours=random.randint(0, 86400)),
                "event_id": event_id,
                "user_id": user_id,
            }
    
    base_features = {
            "click_count": random.randint(0, 20),
            "time_spent": round(random.uniform(0.5, 30.0), 2),
            "scroll_depth": round(random.uniform(0.0, 100.0), 2),
            "purchase_completed": random.randint(0, 1),
            "checkout_time": (base_data["event_time"] + timedelta(hours=random.randint(0, 6))).strftime("%Y-%m-%d %H:%M:%S"),
        }
    if event_id > add_event_interval:
        base_features.update({"ad_interaction": random.randint(0, 5),})
    if event_id > 2 * add_event_interval:
        base_features.update({"session_duration": round(random.uniform(5, 60), 2),})
    if event_id > 3 * add_event_interval:
        base_features.update({"bounce_rate": round(random.uniform(0, 1), 2)})

    base_data.update(base_features)
    base_data["event_time"] = base_data["event_time"].strftime("%Y-%m-%d %H:%M:%S")

    return base_data

def generate_users(num_users):
    """
    Function to generate a list of json users.
    """
    global genreated_users
    users = []
    for i in range(genreated_users, genreated_users + num_users):
        user = generate_user(i)
        users.append(json.dumps(user))
    genreated_users += num_users
    return users

def generate_events(num_events=100, total_users=30, add_event_interval=20, start_date="2024-01-01 00:00:00"):
    """
    Function to generate a list of json events.

    Args:
        num_events: int: Number of events to generate
        total_users: int: Total number of users
        add_event_interval: int: Interval to add additional features a max of 3 new features are added.
    """
    global generated_events
    events = []
    
    for i in range(generated_events, generated_events + num_events):
        user_id = random.randint(1, total_users)
        
        event = generate_event(event_id=i, user_id=user_id, add_event_interval=add_event_interval, start_date=start_date)
        events.append(json.dumps(event))
    generated_events += num_events
    return events