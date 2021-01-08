from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from math import*
import numpy as np
from sympy import *
from pip._vendor.distlib.compat import raw_input
from scipy.integrate import quad

currentPage='index'
description =""
funcName=""
def index(request):
    global currentPage
    currentPage='index'

    return render(request, "index.html", {})

def basic(request):
    global currentPage
    currentPage='basic'

    return render(request, "basic.html", {})

def trigonometry(request):
    global currentPage
    currentPage='trigonometry'

    return render(request, "trigonometry.html", {})

def complex(request):
    global currentPage
    currentPage='complex'

    return render(request, "complex.html", {})

@csrf_protect
def solve(request):
    numbersRaw = request.POST['numbers']
    func=request.POST['func']
    print(numbersRaw)
    print(func)
    numbers=0
    if(not func == 'solDer' and not func == 'solLimit' and not func== 'solIntegral'):
        numbers = [int(x) for x in numbersRaw.split(",")]
    print(numbers)

    
    if(func=='sum'):
        result=add(numbers)
    elif(func=='find_max'):
        result=find_max(numbers)
    elif(func=='find_min'):
        result=find_min(numbers)
    elif(func=='find_range'):
        result=find_range(numbers)
    elif(func=='mode'):
        result=mode(numbers)
    elif(func=='median'):
        result=median(numbers)
    elif(func=='average'):
        result=average(numbers)
    elif(func=='stDev'):
        result=stDev(numbers)

    elif(func=='addition'):
        result=addition(numbers[0],numbers[1])
    elif(func=='subtraction'):
        result=subtraction(numbers[0],numbers[1])
    elif(func=='multiplication'):
        result=multiplication(numbers[0],numbers[1])
    elif(func=='division'):
        result=division(numbers[0],numbers[1])
    elif(func=='squaring'):
        result=squaring(numbers[0])
    elif(func=='finding_factorial'):
        result=finding_factorial(numbers[0])
    elif(func=='exponentiation'):
        result=exponentiation(numbers[0],numbers[1])
    elif(func=='hypotenuse'):
        result=hypotenuse(numbers[0],numbers[1])
    elif(func=='perimeter_of_a_cube'):
        result=perimeter_of_a_cube(numbers[0])
    elif(func=='area_of_a_cube'):
        result=area_of_a_cube(numbers[0])
    elif(func=='perimeter_of_circle'):
        result=perimeter_of_circle(numbers[0])
    elif(func=='area_of_a_circle'):
        result=area_of_a_circle(numbers[0])


    elif(func=='finding_sin'):
        result=finding_sin(numbers[0])
    elif(func=='finding_cos'):
        result=finding_cos(numbers[0])
    elif(func=='finding_tan'):
        result=finding_tan(numbers[0])
    elif(func=='finding_cotan'):
        result=finding_cotan(numbers[0])
    elif(func=='inverse_sin'):
        result=inverse_sin(numbers[0])
    elif(func=='inverse_cos'):
        result=inverse_cos(numbers[0])

    elif(func=='solDer'):
        result=solDer(numbersRaw)
    elif(func=='solLimit'):
        result=solLimit(numbersRaw)
    elif(func=='solIntegral'):
        result=solIntegral(numbersRaw)
    elif(func=='Fibonacci'):
        result=Fibonacci(numbers[0])
    elif(func=='isFibonacci'):
        result=isFibonacci(numbers[0])
    elif(func=='nearestFibonacci'):
        result=nearestFibonacci(numbers[0])
    return render(request, currentPage+".html", {"result": result})

@csrf_protect
def setFunc(request):
    func = request.POST['value']
    print(func)
    print(currentPage)
    if currentPage=='basic':
        [funcName,description]=basicCalculationsSetter(func)
    if currentPage=='index':
        [funcName,description]=staticCalculationsSetter(func)
    if currentPage=='trigonometry':
        [funcName,description]=trigoCalculationsSetter(func)
    if currentPage=='complex':
        [funcName,description]=complexCalculationSetter(func)
    return render(request, currentPage+".html", {"func": func,"description":description,'funcName':funcName})



def basicCalculationsSetter(func):
    if func=='addition':
        funcName='Sum All Numbers'
        description='Addition of two numbers, write numbers in format 1,3 put commas between'
    if func=='subtraction':
        funcName='Substract First Number From Second Number'
        description='Subraction of two numbers, write numbers in format 1,3 put commas between'
    if func=='multiplication':
        funcName='Find Multiplication Number Of the Given Numbers'
        description='Multiplication of two numbers, write numbers in format 1,3 put commas between'
    if func=='division':
        funcName='Find Division Of the Given Numbers'
        description='Division of two numbers, write numbers in format 1,3 put commas between'
    if func=='squaring':
        funcName='Find Square Number Of the Given Number'
        description='Square of number, write numbers in format 5'
    if func=='finding_factorial':
        funcName='Find Factorial Of the Given Number'
        description='Factorial of given number, write numbers in format 5'
    if func=='exponentiation':
        funcName='Find Exponentiation Of the Given Numbers'
        description='Exponentiation of  given number, write numbers in format 5,2 put commas between'
    if func=='hypotenuse':
        funcName='Find Hypotenuse Of the Given Numbers'
        description='Hypotenuse of two numbers, write numbers in format 1,3 put commas between'
    if func=='perimeter_of_a_cube':
        funcName='Find Perimeter Of Cube'
        description='Perimeter of cube, write edge in format 5'
    if func=='area_of_a_cube':
        funcName='Find Area Of Cube'
        description='Area of cube, write edge in format 5'
    if func=='perimeter_of_circle':
        funcName='Find Perimeter Of Circle'
        description='Perimeter of circle, write radius in format 3'
    if func=='area_of_a_circle':
        funcName='Find Area OF Circle'
        description='Area of circle, write radius in format 3'
    print([funcName,description])
    return [funcName,description]
def staticCalculationsSetter(func):
    if func=='sum':
        funcName='Sum All Numbers'
        description='Sum of all numbers, write numbers in format 1,3,4,7 put commas between'
    if func=='find_min':
        funcName='Find Minimum Number Of the Given Numbers'
        description='Min of all numbers, write numbers in format 1,3,4,7 put commas between'
    if func=='find_max':
        funcName='Find Maximum Number Of the Given Numbers'
        description='Max of all numbers, write numbers in format 1,3,4,7 put commas between'
    if func=='find_range':
        funcName='Find Range Of the Given Numbers'
        description='Range of all numbers, write numbers in format 1,3,4,7 put commas between'
    if func=='mode':
        funcName='Find Mode Number Of the Given Numbers'
        description='Mode of all numbers, write numbers in format 1,3,4,7 put commas between'
    if func=='median':
        funcName='Find Median Of the Given Numbers'
        description='Median of all numbers, write numbers in format 1,3,4,7 put commas between'
    if func=='average':
        funcName='Find Average Of the Given Numbers'
        description='Average of all numbers, write numbers in format 1,3,4,7 put commas between'
    if func=='stDev':
        funcName='Find Standard Deviation Of the Given Numbers'
        description='Standard Deviation of all numbers, write numbers in format 1,3,4,7 put commas between'
    if func=='variance':
        funcName='Find Variance Of the Given Numbers'
        description='Variance of all numbers, write numbers in format 1,3,4,7 ,put commas between'
    print([funcName,description])
    return [funcName,description]
def trigoCalculationsSetter(func):
    if func=='finding_sin':
        funcName='Sin Of Degree'
        description='Sin Of Degree, write Degree in format 90'
    if func=='finding_cos':
        funcName='Cos Of Degree'
        description='Cos Of Degree, write Degree in format 90'
    if func=='finding_tan':
        funcName='Tan Of Degree'
        description='Tan Of Degree, write Degree in format 90'
    if func=='finding_cotan':
        funcName='Cot Of Degree'
        description='Cot Of Degree, write Degree in format 90'
    if func=='inverse_sin':
        funcName='ASin Of Degree'
        description='ASin Of Degree, write Degree in format 90'
    if func=='inverse_cos':
        funcName='Acos Of Degree'
        description='Acos Of Degree, write Degree in format 90'
    print([funcName,description])
    return [funcName,description]
def complexCalculationSetter(func):
    if func=='solDer':
        funcName="Derivative Calculate Given Formula"
        description="Example INPUTS:  x^2+1 , sin(x)+x**3"
    if func=='solLimit':
        funcName='Solve Limit'
        description='Example INPUTS:  2 x^2+1  , 0 1/x'
    if func=='solIntegral':
        funcName='Solve Integral'
        description='Example INPUTS:  2 0 x^2+1 or 1 0 sin(x)'
    if func=='Fibonacci':
        funcName='Enter the fibonacci index to get that fibonacci number'
        description='Example INPUT:  5'
    if func=='isFibonacci':
        funcName='Check is the given number is a Fibonacci Number'
        description='Example INPUT:  5'
    if func=='nearestFibonacci':
        funcName='Return the nearest fibonnaci number to given input'
        description='Example INPUT:  5'
    print([funcName,description])
    return [funcName,description]


def sum(numbers):
    return sum(numbers)

def find_max(numbers):
    max=numbers[0]
    i=1
    for i in range(len(numbers)):
        if(max<numbers[i]):
            max=numbers[i]
    return max


def find_min(numbers):
    min=numbers[0]
    i=1
    for i in range(len(numbers)):
        if(min>numbers[i]):
            min=numbers[i]
    return min

def find_range(numbers):
    rng=find_max(numbers)-find_min(numbers)
    return rng

def mode(numbers):
    num = 0
    for i in numbers:
        if numbers.count(i)> numbers.count(num):
            num = i
    return num

def median(numbers):
        numbers.sort()
        length = len(numbers)
        med = int(length / 2)
        if length % 2 == 0:
            return ((numbers[med - 1]) + (numbers[med]))/2
        else:
            return numbers[med]

def average(numbers):
    ssum = 0
    for x in numbers:
        ssum += x
    return ssum / len(numbers)

def stDev(numbers):
    length = len(numbers)
    avg = average(numbers)

    sqr_sum = 0
    for x in numbers:
        sqr_sum += (x-avg)**2
    stdev = math.sqrt(sqr_sum / (length-1))

    return stdev

def variance(numbers):
    return stDev(numbers)**2



def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a * b

def division(a,b):
    return a / b

def squaring(a):
    return a*a

def finding_factorial(a):
    return factorial(a)

def exponentiation(a,b): 
    return a**b

def hypotenuse(a,b):
    return (a*a+b*b)**0.5

def perimeter_of_a_cube(edge):
    return 12*edge

def area_of_a_cube(edge):
    return 6*(edge**2)

def perimeter_of_circle(circle):
    return 2 * math.pi * circle

def area_of_a_circle(circle):
    return (math.pi) * (circle ** 2)



def finding_sin(a):
    return np.sin(a * np.pi/180.)

def finding_cos(a):
    return np.cos(a * np.pi / 180.)

def finding_tan(a):
    return np.tan(a * np.pi /180.)
    
def finding_cotan(a) :
    tan=np.tan(a * np.pi /180.)
    return 1/tan

def inverse_sin(a):
    sin=np.sin(a* np.pi / 180.)
    return np.arcsin(sin)

def inverse_cos(a):  
    cos=np.cos(a * np.pi / 180.)
    return np.arccos(cos)


def solDer(function):
    try:
        tmp = function.split("+")
        print("len of arr: ", len(tmp))
        x = Symbol('x')
        if (len(tmp) == 3):
            upper_bound = sympify(tmp[0])
            # print(upper_bound)
            lower_bound = sympify(tmp[1])
            # print(lower_bound)
            converted = sympify(tmp[2])
            # print(converted)

            answ = integrate(converted, (x, lower_bound, upper_bound))
            return answ
        elif (len(tmp) == 1 or len(tmp)== 2):
            converted = sympify(function)
            answ = converted.diff(x)
            return answ
        else:
            errorString = "You entered your equation in unsuported format please check your equation"
            return errorString

        return answ
    except (SympifyError, TypeError) as e:
        mesage = "Check your input"
        print(e)
        return mesage
        print(mesage)

def solLimit(function):
    try:
        tmp = function.split(' ')
        x = Symbol('x')
        converted = sympify(tmp[1])
        answ = limit(converted, x, tmp[0])
        return answ
    except (SympifyError, TypeError) as e:
        mesage = "Check your input"
        return mesage
        print(mesage)

def drawGraph(function):
    arr = []
    try:

        tmp = function.split(' ')
        name = ""
        if (len(tmp) == 2):
            ran = np.array(range(int(tmp[0])))
            y = sympify(tmp[1])
            name = tmp[1]
        else:
            ran = np.array(range(100))
            y = sympify(function)
            name = function
        fig = plt.figure(figsize=(3, 3), dpi=120,
                         facecolor="lightblue", edgecolor="lightgrey", linewidth=5)

        x = Symbol('x')
        ax = fig.add_axes([0, 0, 1, 1])
        for i in ran:
            arr.append(y.subs(x, i))
        title = "Graph of " + name
        ax.set_title(title)
        plt.plot(ran, arr)
        fig.savefig('graph.png')
        return fig
    except (SympifyError, TypeError) as e:
        mesage = "Check your input"
        return mesage
        print(mesage)


# Function for nth Fibonacci number
 
def Fibonacci(n):
    if n<=0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

def isFibonacci(n):
    n1, n2 = 0, 1
    while True:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        if nth==n:
            return True
            break
        if nth>n:
            return False
            break

def nearestFibonacci(n):
    n1, n2 = 0, 1
    while True:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        a=n2-n1
        if nth==n:
            return n
            break
        if nth>n:
            a=nth-n
            b=n-n1
            if a<b:
                return n2
                break
            else:
                print("l am here")
                return n1
                break

def solIntegral(function):
    try:
        tmp = function.split(" ")
        x = Symbol('x')
        if(len(tmp) == 3):
            upper_bound = sympify(tmp[0])
            lower_bound = sympify(tmp[1])
            converted = sympify(tmp[2])
            answ = integrate(converted,(x,lower_bound,upper_bound))
            return answ
        else:
            return "You entered your equation in unsuported format please check your equation"
    except (SympifyError ,TypeError) as e:
            mesage = "Check your input"
            return mesage