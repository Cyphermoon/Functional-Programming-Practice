modes  =  {
    "uppercase" : "U",
    "lowercase" : "L",
    "punctuation" : "P"
}

def returnPunctuationMap(key):
    punctuationMap = {
        "0" : 0,
        "1" : "!",
        "2" : "?",
        "3" : ",",
        "4" : ".",
        "5" : " ",
        "6" : ":",
        "7"  : '"',
        "8" : "'",
    }

    return punctuationMap.get(key, "0")


def switch_mode(current_mode, modes):
    if current_mode == modes.get("uppercase"):
        return modes.get("lowercase")

    if current_mode == modes.get("lowercase"):
        return modes.get("punctuation")
    
    if current_mode == modes.get("punctuation"):
        return modes.get("uppercase")


def process_digit(digit, mode, modes):
    if mode == modes.get("uppercase"):
        mod = digit % 27
        uppercaseLetter = chr(ord("@") + mod)

        return uppercaseLetter if mod > 0 else 0

    if mode == modes.get("lowercase"):
        mod = digit % 27
        lowercaseLetter = chr(ord("`") + mod)
        return lowercaseLetter if mod > 0 else 0

    if mode == modes.get("punctuation"):
        mod = digit % 9
        return returnPunctuationMap(str(mod))

def main():
    integers = ""
    decoded_msg = ""
    current_mode = modes.get("uppercase")

    while True:
        digits = input("Enter the digit: ")

        if digits == "":
            break

        if digits != "" and digits == ",":
            value = process_digit(int(integers), current_mode, modes=modes)
            integers = ""

            print("Value -> ", value)
            if value == 0:
                current_mode = switch_mode(current_mode, modes=modes)
            else:
                decoded_msg += value

        else:
            integers += digits

    print(decoded_msg)

main()



        
