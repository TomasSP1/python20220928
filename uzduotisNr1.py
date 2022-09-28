

def calculation():
    number = int(input("Write your number in bits ? "))
    bits = number
    bytes = number / 8
    kilobytes = number / 1024
    print(f"calculation in bits is = to {bits}")
    print(f"calculation in bytes is = to {bytes}")
    print(f"calculation in kilobytes is = to {kilobytes}")


calculation()