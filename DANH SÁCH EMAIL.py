emails = set()

with open("CONTACT", "r") as f:
    for line in f:
        email = line.strip().lower()
        if email != "":
            emails.add(email)

for email in sorted(emails):
    print(email)