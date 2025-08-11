inp=input('Enter your name:')
print(f'Hello {inp}, Nice to meet you.')
a=input('How are you feeling today. Good/Bad:')
if a=='Good':
    print(f'{inp} I am glad you are feeling good')
elif a=='Bad':
    print(f'I am sorry to hear that {inp}')
else:
    print('I could not understand')