#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime complexity here is Linear, O(n):
    This is because the value of n is the determining factor in how many operations are performed. Thus, the problem grows linearly, so that as n increases, so do the number of operations. If n = 3, the algorithm requires 3 operations, if n = 4, 4 operations, n = 5, 5 operations, and so on.


b) The runtime complexity here is Quadratic, O(n^2):
    This is because as the value of n grows, the number of operations grows at the same rate.


c) The runtime complexity here is Linear, O(n):
    This is because the function n by 1 each time it is run. Hence, n is the detmining factor on how many operations the function performs.

## Exercise II
    The runtime complexity here is Logarithmic O(log n)

    From the description of the problem, we know the following:
    - There is a building that is n stories tall
    - We have an unlimited amount of eggs, and are testing to see what 
        the highest floor of the building is that the egg can survive a drop.

    - If we choose a floor f at random and it is less than or equal to the survival floor, then the egg remains unbroken: 

    if f <= survival_floor,
        then egg_survival = True

    - If we choose a floor f at random that is higher than the survival floor, then the egg cracks and we have to start again
    if f > survival_floor,
        then egg_survival = False
    
    The goal is to design a way to find the survival_floor number, while also using/losing the least amount of eggs.

    Taking all of this into consideration, a binary search algorithm would be the go to tool.
    1) We can set our variables as follows:
        - n = The total number of floors currently being tested.
        - x = The floor of the building that we are testing: n/2
        - max_n = The highest floor number that is currently included in 
            the current test
        - min_n = The lowest floor number that is currently included in 
            the current test
        - f = The highest floor number that the egg can survive
            - f = min_n, but only if max_n - min_n = 1
    
    
    2) We will start by dropping the egg from the x level, in this case 50.

    3) Then we will check to see if the egg has broken or not.

    4) If the egg is broken, then f must be between min_n and x.
        - If this is the case then reassign max_n to equal the current x value.
    
    5) If the egg is not broken, then f must be between x and max_n.
        - If this is the case, then reassign min_n to equal the current x value.
    
    6) We will repeat this process until we find the highest floor that the egg can survive.

