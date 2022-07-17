#Double every second digit starting for the rightmost digit to the check sum
#When the digit are doubled if they produce to values e.g 7 * 2 = 15, they must be treated has individual digits
#Knowing which digit to double 

identification_number = 1762483


#Double digit
def doubleDigit(digit):
    return digit * 2;

#Sum individual digit
def sumDoubleDigit(digit):
    if(digit >= 10):
        return 1 + (digit % 10)
    else:
        return digit

def checkSumIsValid(digit):
    if digit % 10 == 0:
        return f"checksum is valid. digit is {digit}"
    else: return f"checksum is not valid. digit is {digit}"



def main():
    checksum = 0
    position = 1
    evenLengthCheckSum = 0
    oddLengthCheckSum = 0

    while(True):
        value = input("Enter a single digit value: ")
        if value == "":
            if(position - 1) % 2 == 0:
                checksum += evenLengthCheckSum
            
            else: checksum += oddLengthCheckSum
            break

        if(position % 2 == 0 ):
            oddLengthCheckSum += sumDoubleDigit(doubleDigit(int(value)))
            evenLengthCheckSum += int(value)
        else:
            evenLengthCheckSum += sumDoubleDigit(doubleDigit(int(value)))
            oddLengthCheckSum += int(value)
        
        position += 1

    return checkSumIsValid(checksum)

print(main())



