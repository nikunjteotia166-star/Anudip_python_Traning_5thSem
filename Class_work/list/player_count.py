#program to display score of 11 players!
#taking input of scores for 11 players

scores =[]

for i in range(11):
    score = int(input("enter score:"))
    scores.append(score)

# displaying score

print("scores are:")

for score in scores:
    print(score) 

#---finding highest score---
max_score = scores[0]
for index in range(1 , len(scores)):
    if scores[index] > max_score:
        max_score = scores[index]
print("the highest score is :" , max_score)
