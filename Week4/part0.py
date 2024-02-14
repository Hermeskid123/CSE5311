def fib(n): 
    print("fib call "+str(n)+"->") 
    if n == 0: 
        return 0 
        print("fib Call 0 -> ") 
    if n == 1: 
        return 1 
        print("fib Call 1 ->") 
    res = fib(n-1) + fib(n-2) 
    print("fib Call " + str(res) +"->"  )
    return res
fib(5)
