# wap to input a sentence from user and count the number of special characters present in the sentence

sentence = input("Enter a sentence: ")

count = 0

for ch in sentence:

#check whether special characters are present or not
    if not ch.isalnum() and ch != " ":
        count += 1

print("Number of special characters:", count)
print("------------------------------------")