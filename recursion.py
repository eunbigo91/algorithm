def recursive(input):
    if input <= 0:
        #exit condition. let you know when you need to stop! 
        return input
    else:
        output = recursive(input-1)
        return output

def get_fib(position):
    if (position == 0 or position == 1):
        return position
    return get_fib(position -1) + get_fib(position-2)


