"""
Reads LoL champion data from a CSV file and prints out a concise overview
of champions by role.

The CSV file is expected to have a semicolon as separator and the following
columns:

- id: Unique identifier for the champion
- title: Champion name
- role: Comma-separated list of roles the champion is suitable for
- winrate: Champion winrate
- popularity: Champion popularity
- banrate: Champion banrate

The output is a list of roles, with champions sorted by winrate in descending
order and grouped by role. Each champion is printed with its id, title, winrate,
popularity, and banrate.
"""

import pandas as pd

file_path = 'data\lol_champions.csv'
df = pd.read_csv(file_path, sep=';')

champion_roles = {}

for index, row in df.iterrows():
    roles = row['role'].split(',')
    for role in roles:
        if role not in champion_roles:
            champion_roles[role] = []
        champion_roles[role].append({
            'id': row['id'],
            'title': row['title'],
            'winrate': row['winrate'],
            'popularity': row['popularity'],
            'banrate': row['banrate']
        })

for role, champions in champion_roles.items():
    print(f"Role: {role}")
    for champ in sorted(champions, key=lambda x: x['winrate'], reverse=True):
        print(f"  - {champ['id']} '{champ['title']}' (Winrate: {champ['winrate']:.2%}, Popularity: {champ['popularity']:.2%}, Banrate: {champ['banrate']:.2%})")
