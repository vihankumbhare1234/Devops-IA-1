import json
import os
from datetime import datetime

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

# Predefined users
users = {
    "user1@example.com": "password123",
    "user2@example.com": "mypassword",
    "admin@example.com": "admin123"
}

# Ask user input
email = input("Enter your email: ").strip()
password = input("Enter your password: ").strip()

# Verify credentials
status = "SUCCESS" if email in users and users[email] == password else "FAILURE"
message = "Logged in successfully" if status == "SUCCESS" else "Failed to login"

# Print to console
print(f"{message} for {email}")

# Create a structured log entry
log_entry = {
    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "email": email,
    "status": status,
    "message": message
}

# Append log entry as JSON to file
log_file = "./logs/login.log"
with open(log_file, "a") as f:
    f.write(json.dumps(log_entry) + "\n")
