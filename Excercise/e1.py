# numStart=1500
# numEnd=2700
 
# for i in range(numStart, numEnd+1):
#     dv7=i%7
#     dv5=i%5
    
#     if(dv7==0):
#         print('Divisible by 7', i)
    
#     if(dv5==0):
#         print('Divisible by 5', i)

# Excercise 2
# numbers=[1,2,3,4,5,6,7,8,9]
# countEven=0
# countOdd=0
# for i in numbers:
#     v=i%2
#     if(v==0):
#         countEven=countEven+1
#     elif(v!=0):
#         countOdd=countOdd+1

# print('Number of Even numbers', countEven)
# print('Number of Odd numbers', countOdd)

# Excercise 3 - Factorial

# number = 8
# c=1
# for i in range(1,int(number)+1):
#     if(i!=0):
#         c=i*c
#         # print(c)

# print("The factorial of",number,"is",c)

# help(str)

# print("hello{v1}, How are you? {v2}".format(v1=" ava", v2=" asdf"))

# n=400
# print(id(n))
# n=8
# print(id(n))
# n=400
# print(id(n))

 

# print(100*100)
# print(9999+8888)
# print(9999+8888 + 100*100) 

# def sum(x, y):
# 		return(x+y)
# print(sum(sum(1,2), sum(3,4)))

# print(((10 >= 5*2) and (10 <= 5*2)))


# def square(n):
#     return n*n

# def sum_squares(x):
#     sum = 0
#     for n in range(x):
#         sum += square(n)
#         print(n)
#     return sum

# print(sum_squares(10)) # Should be 285

# def sum_positive_numbers(n):
#     # The base case is n being smaller than 1
#     if n < 1:
#         return 1

#     # The recursive case is adding this number to 
#     # the sum of the numbers smaller than this one.
#     return n +  sum_positive_numbers(n-1)

# print(sum_positive_numbers(3)) # Should be 6
# print(sum_positive_numbers(5)) # Should be 15

# function which return reverse of a string 

def isPalindrome(s): 
	return s == s[::-1] 


# Driver code 
s = "malayalam"
ans = isPalindrome(s) 

if ans: 
	print("Yes") 
else: 
	print("No")  


# function to check string is 
# palindrome or not 
def isPalindrome(str): 

	# Run loop from 0 to len/2 
	for i in range(0, int(len(str)/2)): 
		if str[i] != str[len(str)-i-1]: 
			return False
	return True

# main function 
s = "malayalam"
ans = isPalindrome(s) 

if (ans): 
	print("Yes") 
else: 
	print("No") 

num=str("navin")
temp=num
rev=0
while(int(len(num))>0):
    dig=int(len(num))%10
    rev=rev*10+dig
    num=num//10
print(temp,rev)
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")

strip()