import os
from datetime import datetime

# Path to your repository
REPO_DIR = os.getcwd()  # use current directory

# File to update daily
filename = "activity_log.txt"
filepath = os.path.join(REPO_DIR, filename)

# Append current timestamp to file
with open(filepath, "a") as f:
    f.write(f"Daily update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

print(f"Updated {filename} successfully!")
