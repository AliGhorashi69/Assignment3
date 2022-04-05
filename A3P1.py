import random

words = ['book', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste', 'shirmoz']

# i = random.randint(0, len(words)-1)
# word = words[i]

word = random.choice(words) # clock
word=word.casefold() #to eliminate the upper/lower case sensitivity
joon = len(word)*2



while joon > 0:
    print('- ' * len(word)) 
    

    user_character = input() # s
    user_character=user_character.casefold()# to remove upper/lower case sensitivity
    

    if user_character=="exit":
        joon=0
        break

    if user_character in word:
        
        print('yes')
    
        if user_character==word:
            break
    else:
        joon = joon - 1
        print('no')
        if joon==0:
            break


if joon>0:
    print("You Won!!!  :) ")
else:
    print("You Lost the Game !!! :( The Answer is: ", word)