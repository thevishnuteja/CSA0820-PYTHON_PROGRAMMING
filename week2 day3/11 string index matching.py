def count_matching_chars(s1, s2):
    count = 0
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            count += 1
    return count

# Sample input
s1 = "what"
s2 = "watch"
matches = count_matching_chars(s1, s2)
print("Number of matching characters:", matches)
