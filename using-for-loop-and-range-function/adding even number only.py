target=int(input())
even_sum=0
for number in range(2,target+1,2):
    even_sum+=number
print(even_sum)




#alternative
sum=0
for num in range(1,target+1):
    if num%2==0:
        sum+=num
print(sum)