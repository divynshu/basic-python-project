#FizzBuzz is a game where people have to count the number
#If number is divisible by 3 you have to say "Fizz".
#if number is divisible by 3 you have to say "Buzz".
#I number divisible by both 3 and 5 both then say "FizzBuzz"
target=100
for number in range(1,target+1):
    if number % 3 == 0 and number % 5 == 0 :
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else :
        print(number)