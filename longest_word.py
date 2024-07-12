sentence = input("enter the sentence")
longest = max(sentence.split(), key=len)
print("Longest word is: ", longest)
print("And its length is: ", len(longest))
