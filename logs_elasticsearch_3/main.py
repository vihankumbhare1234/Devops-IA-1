import time
import random
import os
from datetime import datetime

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

# Log file path
log_file = "logs/app1.log"

# Sample random English sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "I love programming in Python.",
    "Fluentd makes log management easy.",
    "Docker containers simplify deployment.",
    "Learning new things every day keeps you sharp.",
    "Artificial Intelligence is the future of technology.",
    "Data science is both challenging and rewarding.",
    "Always keep your code clean and readable.",
    "Debugging can sometimes be fun.",
    "Consistency is key to mastering any skill.",
    "Reading books expands your knowledge.",
    "Writing tests improves software quality.",
    "Practice makes perfect.",
    "Collaboration leads to better solutions.",
    "Innovation drives progress.",
    "Automation saves time and reduces errors.",
    "Understanding algorithms is essential.",
    "Stay curious and keep exploring.",
    "Technology changes rapidly, adapt quickly.",
    "Good communication improves teamwork."
]

# Generate 20 log messages
for i in range(20):
    message = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "message": random.choice(sentences)
    }

    # Print to console
    print(message)

    # Append as JSON to log file
    with open(log_file, "a") as f:
        f.write(str(message).replace("'", '"') + "\n")

    # Wait 5-10 seconds
    time.sleep(random.randint(5, 10))
