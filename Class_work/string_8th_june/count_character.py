#write a program to input a string and input a sentence from user and count the num of character present in it without using len function
text = input("Enter a string or sentence: ")

count = 0

for ch in text:
    count += 1

print("Number of characters in text:", count)  