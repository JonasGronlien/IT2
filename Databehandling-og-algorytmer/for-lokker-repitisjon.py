actors = [
    {"name": "Tom Hanks", "age": 66},
    {"name": "Meryl Streep", "age": 73},
    {"name": "Leonardo DiCaprio", "age": 48},
    {"name": "Julia Roberts", "age": 55},
    {"name": "Denzel Washington", "age": 67},
    {"name": "Nicole Kidman", "age": 55},
    {"name": "Brad Pitt", "age": 59},
    {"name": "Charlize Theron", "age": 47},
    {"name": "Johnny Depp", "age": 59},
    {"name": "Emma Stone", "age": 34},
]

størst = float("-inf")
for actor in actors:
    print(f"{actor['name']} er {actor['age']} år gammel")
    if actor["age"] > størst:
        størst = actor["age"]
        størst_navn = actor['name']
        
print(f"Den eldste skuespilleren er {størst_navn} som er {størst} år gammel")

eldst = actors[0]
for actor in actors:
    if actor['age'] > eldst['age']:
        eldst = actors

print(f"Den eldste skuespilleren er {eldst['name']} som er {eldst['age']} år gammel")


