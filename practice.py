def twenty():
    annual_salary=int(input())
    tax_rate=int(input())
    post_tax_annual_salary=annual_salary*(1-tax_rate//100)
    monthly_salary=post_tax_annual_salary//12
    print(monthly_salary)

def twentyone():
    celsius_temperature=int(input())
    ft=celsius_temperature*9//5+32
    kt=celsius_temperature+273.15
    print("Fahrenheit temperature = ",ft)
    print("Kelvin temperature = ",kt)

def twentytwo():
    a=int(input())
    b=int(input())
    if a>b:
        print(a-b)
    else:
        print(b-a)

def twentythree():
    a=int(input())
    b=int(input())
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(a,b)

def twentyfour():
    a=int(input())
    b=int(input())
    c=int(input())
    if a>b:
        if a>c:
            print(a)
        else: 
            print(c)
    else:
        if b>c:
            print(b)
        else:
            print(c)

def twentyfive():
    a=int(input())
    if a>0:
        print(a)
    else:
        print((-1)*a)
    
def twentysix():
    n=int(input())
    if n & 1:
        print("Odd")
    else:
        print("Even")

def twentyseven():
    marks=int(input())
    if marks>90:
        print("A+")
    elif marks>80:
        print("A")
    elif marks>70:
        print("B+")
    elif marks>60:
        print("C")
    elif marks>50:
        print("D")
    else:
        print("Fail")

def twentyEight():
    pass_type=input().lower()
    coach_type=input().lower()
    if pass_type =="one-time journey":
        if coach_type=="sleeper":
            print("300")
        elif coach_type=="3ac":
            print("400")
        elif coach_type=="2ac":
            print("500")
        else:
            print("600")
    else:
        if coach_type=="sleeper":
            print(30*300)
        elif coach_type=="3ac":
            print(30*400)
        elif coach_type=="2ac":
            print(30*500)
        else:
            print(30*600)
        
def odd_number():
    n=int(input())
    for i in range(1,n,2):
        print(i)

def first_n_odd_number():
    n=int(input())
    for i in range(2*n):
        if i%2!=0:
            print(i)
def thirty():
    a=list(map(int,input().split()))
    if a[0]+a[1]>a[2] and a[1]+a[2]>a[0] and a[0]+a[2]>a[1]:
        print("Yes")
    else:
        print("No") 

def thirtyone():
    a=int(input())
    ans=1
    for i in range(1,a+1):
        ans*=i
    print(ans)

def thirtytwo():
    a=int(input())
    flag=True
    for i in range(2,int(a**0.5) + 1):
        if a%i==0:  
            flag=False
            break
        else:
            continue
    if flag:
        print("yes")
    else:
        print("No")

def thirtythree():
    n=int(input())
    first_term=int(input())
    common_ratio=int(input())
    ans=first_term
    for i in range(1,n+1):
        print(ans,end=" ")
        ans*=common_ratio

def thirtyfour():
    n=int(input())
    number=list(map(int,input().split()))
    sum=0
    for i in range(len(number)):
        sum+=number[i]
    print(sum)

def thirtyfive():
    n=int(input())
    for i in range(0,n):
        for j in range(0,n):
            print(i,j)

def thirtysix():
    n=int(input())
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print()

def thirtyseven():
    rows = int(input())
    columns = int(input())
    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()



def thirtyeight():
    n=int(input())
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print()

def forty():
    n=int(input())
    power = 1
    while power < n:
        power *= 2
    if abs(power - n) < abs(power//2 - n):
        print(power)
    else:
        print(power//2)

def fortyone():
    n=int(input())
    totalsum=0
    while n>0:
        totalsum += n % 10
        n //= 10
    print(totalsum)

def fortytwo():
    n=int(input())
    
def reverse_a_string():
    str=input()
    reverse_str=str[::-1]
    print(reverse_str)

def palindrome():
    str=input()
    reverse_str=str[::-1]
    if(str==reverse_str):
        print("Yes\n")
    else:
        print("No\n")

def left_shift():
    str=input()
    k=int(input())
    left_shift_str=str[k:]+str[0:k]
    print(left_shift_str)



def sumofelementsinarray():
    lis=list(map(int,input().split()))
    sum=0
    for i in range(len(lis)):
        sum+=lis[i]
    print(sum)

def sumofoddandindicesinarray():
    lis=list(map(int,input().split()))
    sum_odd=0
    sum_even=0
    for i in range(len(lis)):
        if i%2==0:
            sum_even+=lis[i]
        else:
            sum_odd+=lis[i]
    print(abs(sum_odd-sum_even))        

def palindrome():
    lis=list(map(int,input().split()))
    flag=True
    for i in range(len(lis)):
        if lis[i]==lis[len(lis)-1-i]:
            continue
        else:
            flag=False
            break
    if flag:
        print("Yes")
    else:
        print("No")

def adjacent_value_sum():
    lis=list(map(int,input().split()))
    new_lis=[]
    sum=0    
    for i in range(len(lis)-1):
        x=lis[i]+lis[i+1]
        sum+=x
        new_lis.append(x)
    print(new_lis)

def prefix_sum():
    lis=list(map(int,input().split()))
    prefix_array=[]
    prefix_array.append(lis[0])
    for i in range(1,len(lis)):
        x=prefix_array[i-1]+lis[i]
        prefix_array.append(x)
    print(prefix_array)

def check_if_array_represent_fibonacci_sequence_or_not():
    lis=list(map(int,input().split()))
    x=len(lis)
    fibonacci_array=[1,1]
    for i in range(2,len(lis)):
        fibonacci_array.append(fibonacci_array[i-2]+fibonacci_array[i-1])

    if(fibonacci_array==lis):
        print("Yes")
    else:
        print("NO")

def sum_of_each_row_in_2d_array():
    n = int(input("Enter the number of rows:")) 
    m = int(input("Enter the number of columns:")) 
  
    matrix = [] 

    print("Enter values in matrix :") 

# For user input 
    for i in range(n):
        data =[] 
        for j in range(m):
            data.append(int(input())) 
        matrix.append(data) 

# For printing the matrix 
    for i in range(n): 
        for j in range(m): 
            print(matrix[i][j], end = " ") 
        print()


# For printing row wise sum 
    for i in range(n):
        sum = 0
        for j in range(m): 
            sum = sum + matrix[i][j]
        print('Sum of row',i+1,':',sum)

sum_of_each_row_in_2d_array()

    


