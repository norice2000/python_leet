from collections import Counter
votes = [ "champ", "lulu", "lulu", "lucky", "champ" , "champ"]

vote_counts = Counter(votes)

print(f"How many votes champ got?: {vote_counts['champ']}")

vote_counts.up