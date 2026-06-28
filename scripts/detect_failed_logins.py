import re
from collections import Counter

LOG_FILE = "logs/auth.log"

failed_login_pattern = re.compile(
    r"Failed password for (invalid user )?(?P<user>\w+) from (?P<ip>\d+\.\d+\.\d+\.\d+)"
)

failed_ips = Counter()
failed_users = Counter()

with open(LOG_FILE, "r") as file:
    for line in file:
        match = failed_login_pattern.search(line)
        if match:
            ip = match.group("ip")
            user = match.group("user")

            failed_ips[ip] += 1
            failed_users[user] += 1

print("\n=== Failed Login Detection Report ===\n")

print("Failed login attempts by IP:")
for ip, count in failed_ips.items():
    print(f"{ip}: {count}")

print("\nTargeted usernames:")
for user, count in failed_users.items():
    print(f"{user}: {count}")

print("\nPotential brute-force indicators:")
for ip, count in failed_ips.items():
    if count >= 3:
        print(f"ALERT: {ip} had {count} failed login attempts")
