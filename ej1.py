DATA_PATH = 'data/ej1.txt'

digits_p1 = {str(i): i for i in range(10)}

written_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

digits_p2 = {**digits_p1, **{dig:  i for i, dig in enumerate(written_digits)}}

def get_first_digit(str, valid_digits):
    i = 0
    while i<len(str):
       if str[i] in valid_digits:
            return valid_digits[str[i]]
       elif i<len(str)-3 and str[i:i+3] in valid_digits:
            return valid_digits[str[i:i+3]]
       elif i<len(str)-4 and str[i:i+4] in valid_digits:
            return valid_digits[str[i:i+4]]
       elif i<len(str)-5 and str[i:i+5] in valid_digits:
            return valid_digits[str[i:i+5]]
       
       i += 1

def compute_calibration(valid_digits):
    with open(DATA_PATH) as file:
        result = 0
        valid_digits_rev = {dig[::-1]: v for dig, v in valid_digits.items()}
        for line in file:
            result += 10*get_first_digit(line, valid_digits) + get_first_digit(line[::-1], valid_digits_rev)

    return result

def main():
    print(f"Result of part 1 is {compute_calibration(valid_digits=digits_p1)}")
    print(f"Result of part 2 is {compute_calibration(valid_digits=digits_p2)}")


if __name__ == "__main__":
    main()