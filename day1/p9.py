#program to check if letter is vowel or consonant

character = input('enter any letter to check if it is vowel or consonant ')
if(character =='a' or  character=='e' or character =='i' or character =='u'):
    print(f'{character} is a Vowel')
elif(character =='A' or character =='E' or character =='I' or character =='U'):
    print(f'{character} is a Vowel')
else:
    print(f'{character} is a consonant')