def group_anagrams(strings):
    from collections import defaultdict
    anagrams=defaultdict(list)
    for s in strings:
        key=''.join(sorted(s.lower()))
        anagrams[key].append(s)
    return list(anagrams.values())
strings=["Eat", "Tea", "Tan", "Ate", "Nap", "Bat"]
group_anagrams=group_anagrams(strings)
print(group_anagrams)
