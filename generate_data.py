import json
import random
import time
from datetime import datetime

generated_events = 0
genreated_users = 0

# New features to introduce over time
new_features = {
    "ad_interaction": lambda: random.randint(0, 5),
    "session_duration": lambda: round(random.uniform(5, 60), 2),
    "bounce_rate": lambda: round(random.uniform(0, 1), 2)
}

# Generate user data
def generate_user(user_id):
    return {
        "user_id": user_id,
        "age": random.randint(18, 65),
        "location": random.choice(["USA", "Canada", "UK", "Germany", "India", "Australia"]),
        "subscription_status": random.choice(["free", "premium", "trial"])
    }

def generate_event(event_id, user_id, add_event_interval):
    base_features = {
            "click_count": random.randint(0, 20),
            "time_spent": round(random.uniform(0.5, 30.0), 2),
            "scroll_depth": round(random.uniform(0.0, 100.0), 2),
            "purchase_amount": round(random.uniform(0.0, 500.0), 2)
        }
    if event_id > add_event_interval:
        base_features.update({"ad_interaction": random.randint(0, 5),})
    if event_id > 2 * add_event_interval:
        base_features.update({"session_duration": round(random.uniform(5, 60), 2),})
    if event_id > 3 * add_event_interval:
        base_features.update({"bounce_rate": round(random.uniform(0, 1), 2)})

    base_data = {
                "event_time": datetime.utcnow().isoformat(),
                "event_id": event_id,
                "user_id": user_id,
            }
    base_data.update(base_features)

    return base_data

def generate_users(num_users):
    global genreated_users
    users = []
    for i in range(genreated_users, genreated_users + num_users):
        user = generate_user(i)
        users.append(json.dumps(user))
    genreated_users += num_users
    return users

def generate_events(num_events=100, total_users=30, add_event_interval=20):
    global generated_events
    events = []
    users = {}
    feature_keys = list(new_features.keys())
    
    for i in range(generated_events, generated_events + num_events):
        user_id = random.randint(1, total_users)
        
        event = generate_event(event_id=i, user_id=user_id, add_event_interval=add_event_interval)
        events.append(json.dumps(event))
    generated_events += num_events
    return events