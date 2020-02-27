isbn = input("Enter your ISBN: ")
first_sum =0
second_sum=0

for i in range(0,12,2):
    first_sum = first_sum + int(isbn[i]) 
for i in range(1,12,2):
    second_sum = second_sum  + 3*int(isbn[i])

thirteenth = 10 - (first_sum + second_sum) %10
print(thirteenth)



