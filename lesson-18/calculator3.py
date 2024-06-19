import logging

logger = logging.getLogger('custom_logger')
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('calculator.log')
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

# Create formatters and add to handlers
console_format = logging.Formatter('%(message)s')
file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

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
        math_operation = add(nums)
    elif '-' in text:
        nums = text.split('-')
        math_operation = sub(nums)
    elif '*' in text:
        nums = text.split('*')
        math_operation = mul(nums)
    elif '/' in text:
        nums = text.split('/')
        math_operation = div(nums)
    else:
        print("Invalid input")
    
    logger.info(f"{text} = {math_operation}")

run_calculator()