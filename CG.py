
def fizzBuzz(n):
    i=1
    # Write your code here
    while i<=n:
        if (i%3==0) and (i%5==0):
            print("FizzBuzz")
            i+=1
        elif (i%3==0) and (i%5!=0):
            print("Fizz")
            i+=1
        elif (i%5==0) and (i%3!=0):
            print("Buzz")
            i+=1
        else:
            print(i)
            i+=1
n=int(input())
fizzBuzz(n)
print("Hola Mundo!")



