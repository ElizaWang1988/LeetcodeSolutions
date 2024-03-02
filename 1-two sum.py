nums=[2,7,11,15]
dices=[]
target=9
#print(len(nums))
for i, num1 in enumerate(nums):
    for j, num2 in enumerate(nums[i+1:], start=i+1):
        print(i,j)
        if num1 + num2 == target:
           dice=(i,j)
           dices.append(dice)
print(dices)
       

# sum=[2,3,4,5,6,7,8]
# sum.insert(9,'du')
# print(sum)
# sum.insert(7,'xu')
# print(sum)

# ti=['fbh','djh','di','duh','didh','gok','jwi','ooj']
# for i in ti:
#     print(i)
