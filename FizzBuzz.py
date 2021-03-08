# return 0 if not fizz 1 if fizz
def is_Fizz(a):
    if int(a) % 3 == 0:
        return 1
    else:
        return 0

# return 0 if not Buzz 1 if Buzz
def is_Buzz(a):
    if int(a) % 5 == 0:
        return 1
    else:
        return 0

def print_num():
    num_array = list(range(1, 101))
    return num_array

def main():
    temp = print_num()
    a = int(0)
    y = int(0)
    z = int(0)
    for x in temp:
        print(x)
        if is_Fizz(x) == 1 and is_Buzz(x) == 1:
            print("FizzBuzz\n")
            y += 1
        elif is_Fizz(x) == 1:
            print("Fizz\n")
            a += 1
        elif is_Buzz(x) == 1:
            print("Buzz")
            z += 1
    # print("A is: ", a)
    # print("Y is: ", y)
    # print("Z is: ", z)
    if y == 6 and a == 27 and z == 14:
        #print("returned 1")
        return 1
    else:
        #print("returned 0")
        return 0

if __name__ == '__main__':
    main()
