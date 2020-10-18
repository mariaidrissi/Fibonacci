def fibonacci(nb):
    if(nb <= 1):
            return nb
    else:
            return (fibonacci(nb-1) + fibonacci(nb-2))