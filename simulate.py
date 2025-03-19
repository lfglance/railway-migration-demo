#!/usr/bin/env python3

from random import choice
from secrets import token_urlsafe

import requests


names = [
    "Emma", "Liam", "Olivia", "Noah", "Ava", "Ethan",
    "Sophia", "Mason", "Isabella", "James", "Mia", "Alexander",
    "Charlotte", "Michael", "Amelia", "Elijah", "Harper", "William",
    "Evelyn", "Benjamin", "Abigail", "Lucas", "Emily", "Logan",
    "Elizabeth", "Oliver", "Sofia", "Daniel", "Avery", "Jackson"
]

if __name__ == "__main__":
    for i in range(1000):
        players = []
        for i in range(2):
            new_user = f"{choice(names)}-{token_urlsafe(6)}"
            registration = requests.post("http://127.0.0.1:5000/register", json={"name": new_user})
            registration.raise_for_status()
            session = requests.post("http://127.0.0.1:5000/authenticate", json={"name": new_user})
            players.append(new_user)
            print(f"created {new_user}")

        match = requests.post("http://127.0.0.1:5000/play", json={"player_1": players[0], "player_2": players[1]})
        match.raise_for_status()
        print(match.json())

