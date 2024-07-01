# Authour : Mohamed Saad Taha Mohamed
# College : Faculty of Computers and Artificial Intelligence,Cairo University

def decimal_to_binary(your_num):
    binResult = ""
    if your_num== 0:
        return "0"
    while your_num> 0:
        rem = your_num% 2
        binResult = str(rem) + binResult
        your_num//= 2
    return binResult

def binary_to_decimal(your_num):
    DeciResult = 0
    your_num = str(your_num)
    for i in range(len(your_num)):
        bit = int(your_num[i])
        DeciResult += bit * (2 ** (len(your_num) - 1 - i))
    return DeciResult

def hexadecimal_to_octal(your_num):
    hex_chars = "0123456789ABCDEF"
    octResult = ""
    decimal_result = 0
    for hex_digit in your_num:
        decimal_result = decimal_result * 16 + hex_chars.index(hex_digit)
    while decimal_result > 0:
        rem = decimal_result % 8
        octResult = str(rem) + octResult
        decimal_result //= 8
    return octResult

def decimal_to_octal(your_num):
    your_num = int(your_num)
    OctResult = ""
    if your_num == 0:
        return "0"
    while your_num > 0:
        rem = your_num % 8
        OctResult = str(rem) + OctResult
        your_num //= 8
    return OctResult

def hexadecimal_to_binary(your_num):
    hexaSympol = "0123456789ABCDEF"
    BinNums = "0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111".split()
    your_num= your_num.upper()
    binResult = ""
    for digit in your_num:
        if digit in hexaSympol:
            index = hexaSympol.index(digit)
            binResult += BinNums[index]
    return binResult

def decimal_to_hexadecimal(your_num):
    hexaResult = ""
    if your_num== 0:
        return "0"
    hexaSympol = "0123456789ABCDEF"
    while int(your_num)> 0:
        rem = int(your_num)% 16
        hexaResult = hexaSympol[rem]+hexaResult
        your_num=int(your_num)//16
    return hexaResult

def octal_to_decimal(your_num):
    DeciResult = 0
    for i in range(len(your_num)):
        digit = int(your_num[i])
        DeciResult += digit * (8 ** (len(your_num) - 1 - i))
    return DeciResult

def hexadecimal_to_decimal(your_num):
    hex_chars = "0123456789ABCDEF"
    decimal_result = 0
    for hex_digit in your_num:
        decimal_result = decimal_result * 16 + hex_chars.index(hex_digit)
    return decimal_result

def show_men1():
    print("** numbering system converter **")
    print("A) Insert a new number")
    print("B) Exit program")

def show_men2():
    print("** Please select the base you want to convert a number from **")
    print("A) Decimal")
    print("B) Binary")
    print("C) Octal")
    print("D) Hexadecimal")

def show_men3():
    print("** Please select the base you want to convert a number to **")
    print("A) Decimal")
    print("B) Binary")
    print("C) Octal")
    print("D) Hexadecimal")

while True:
   show_men1()
   choose_men1= input("Enter your choose (A/B): ").upper()
   if choose_men1 == "B":
       break
   if choose_men1 !="A"and"B":
       print("Please select a valid choose")
       continue
   if choose_men1== "A":
        your_num=(input("please insert a number"))
        show_men2()
        choose_men2 = input("Enter your choose (A/B/C/D): ").upper()

   if choose_men2 in ['A', 'B', 'C', 'D']:
        show_men3()
        choose_men3 = input("Enter your choose (A/B/C/D): ").upper()
        if choose_men3 in ['A', 'B', 'C', 'D']:
            if choose_men2 == 'A' and choose_men3 =='B':
                print(decimal_to_binary(int(your_num)))

            elif choose_men2 == 'A'and choose_men3 =='A':
                print(your_num)

            elif choose_men2 == 'A'and choose_men3 =='C':
                print(decimal_to_octal(int(your_num)))

            elif choose_men2 == 'A'and choose_men3 =='D':
                print(decimal_to_hexadecimal(int(your_num)))

            elif choose_men2 =='B'and choose_men3 =='A':
                print(binary_to_decimal(your_num))

            elif choose_men2 =='B'and choose_men3 =='B':
                print(your_num)

            elif choose_men2 =='B'and choose_men3 =='C':
                print(decimal_to_octal(int(binary_to_decimal(your_num))))

            elif choose_men2 =='B'and choose_men3 =='D':
                print(decimal_to_hexadecimal(int(binary_to_decimal(your_num))))

            elif choose_men2 =='C'and choose_men3 =='A':
                print(octal_to_decimal(your_num))

            elif choose_men2 =='C'and choose_men3 =='B':
                print(octal_to_decimal(decimal_to_binary(int(your_num))))

            elif choose_men2 =='C'and choose_men3 =='C':
                print(your_num)

            elif choose_men2 =='C'and choose_men3 =='D':
                print(decimal_to_hexadecimal(int(octal_to_decimal(your_num))))

            elif choose_men2 =='D'and choose_men3 =='A':
                print(hexadecimal_to_decimal(your_num))

            elif choose_men2 =='D'and choose_men3 =='B':
                print(hexadecimal_to_binary(your_num))

            elif choose_men2 =='D'and choose_men3 =='C':
                print(hexadecimal_to_octal(your_num))

            elif choose_men2 =='D'and choose_men3 =='D':
                print(your_num)