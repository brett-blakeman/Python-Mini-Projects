word = input("Enter a word: ")
vowels = "aeiouAEIOU"

vowCount = 0
acount = 0
ecount = 0
icount = 0
ocount = 0
ucount = 0

for letter in word:
    if letter in vowels:
        vowCount += 1
        if letter == 'a' or letter == 'A':
            acount += 1
        elif letter == 'e' or letter == 'E':
            ecount += 1
        elif letter == 'i' or letter == 'I':
            icount += 1
        elif letter == 'o' or letter == 'O':
            ocount += 1
        elif letter == 'u' or letter == 'U':
            ucount += 1

print(f"The number of vowels in '{word}' is {vowCount}.")
print(f"The number of consonants in '{word}' is {len(word) - vowCount}.")
print(f"The number of 'a's in '{word}' is {acount}.")
print(f"The number of 'e's in '{word}' is {ecount}.")
print(f"The number of 'i's in '{word}' is {icount}.")
print(f"The number of 'o's in '{word}' is {ocount}.")
print(f"The number of 'u's in '{word}' is {ucount}.")