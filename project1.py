import random
print('welcome to the game')
_phrase = [['learn', 'from', 'yesterday'], ['be', 'the', 'change'], ['do', 'your', 'best'], ['follow', 'your', 'heart'],
           ['never', 'give', 'up']]

_random_phrase = random.randint(0, 4)
ans = _phrase[_random_phrase]
print(ans)
_under = [len(word) * '_' for word in ans]

print(_under)

score = 0


while _under != ans:
    guessed_letter = input('guess the letter: ')
    if not guessed_letter.isalpha():
        print('guess only a letter')
    elif len(guessed_letter) > 1:
            print('guess only one letter')
    guess = 0
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            if ans[i][j] == guessed_letter:
                _under[i] = _under[i][:j]+guessed_letter+_under[i][j+1:]
                guess =+ 1

        if guess != 0:
            score += 1


    print(_under)
    print(score)

print('you finished the game')
