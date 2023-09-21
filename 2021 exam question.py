def is_anagram(w1,w2):
    if sorted(w1) == sorted(w2) :
        return True
    else:
        return False
    
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

w1u = word1.upper()

w2u = word2.upper()


if(sorted(w1u)) == (sorted(w2u)):
    #print("YES")
    print(word1,"is an anagram of", word2)
elif (sorted(w1u)) == (sorted(w2u)):
    print(word1,"is not an anagram of", word2)
    
ANS = is_anagram(w1u,w2u)

if ANS == True:
    print(word1,"is an anagram of", word2)
else :
    print(word1,"is not an anagram of", word2)
    
phrase = input("Enter a phrase: ")
phrase0Spaces = phrase.replace(" ", "")
finalPhrase = phrase0Spaces.upper()
if (is_anagram(w1u, finalPhrase)):
    print(word1,"is an anagram of", phrase)
else:
    print(word1,"is not an anagram of", phrase)

if (is_anagram(w2u, finalPhrase)):
    print(word2,"is an anagram of", phrase)
else:
    print(word2,"is not an anagram of", phrase)
    



    
    