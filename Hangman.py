import random
words = ["office", "panda", "ginger", "cabin"]
random_word = random.choice(words)
# the dash in word
display = ["_"] * len(random_word)
print(" ".join(display))
life = 6
while "_" in display and life > 0 :
    guessed = input("Enter your letter :").lower()
    if guessed not in random_word:
        life -= 1
#index guessed ...
    for position in range(len(random_word)):
        if random_word[position] == guessed:
            display[position] = guessed
    print(" ".join(display))
    print(f"You have {life} more tries")
if life == 0 :
    print("""
    YOU LOST
    """)
    print(r"""
       ----+
       |    |
       o    |
      /|\   |
      / \   |
    ========
    """)
else :
    print("""
      ***** 
     YOU WIN
      ***** 
    """)
