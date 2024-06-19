

def add(nums):
    total = 0
    for num in nums:
        total += float(num)
    return total

def sub(nums):
    total = 0
    for num in nums:
        total -= float(num)
    return total

def mul(nums):
    total = 1
    for num in nums:
        total *= float(num)
    return total

def div(nums):
    total = 1
    for num in nums:
        total /= float(num)
    return total


def run_calculator():

    text = input("math operation : ")
    if '+' in text:
        nums = text.split('+')
        print(add(nums))
    elif '-' in text:
        nums = text.split('-')
        print(sub(nums))
    elif '*' in text:
        nums = text.split('*')
        print(mul(nums))
    elif '/' in text:
        nums = text.split('/')
        print(div(nums))
    else:
        print("Invalid input")

run_calculator()