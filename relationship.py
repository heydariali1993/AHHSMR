# Initially, Ali considers Harshana and Maria as colleagues
relationships = {
    "Harshana": "colleague",
    "Maria": "colleague"
}

print("Initially:")
for person, status in relationships.items():
    print(f"- Ali and {person} are {status}s.")

print("\nTime passes, and through collaboration and shared experiences, bonds are formed...")

# Over time, Ali now considers them friends
relationships["Harshana"] = "friend"
relationships["Maria"] = "friend"

print("\nEventually:")
for person, status in relationships.items():
    print(f"- Ali and {person} have become {status}s.")