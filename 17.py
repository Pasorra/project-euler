def count_letters(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundred = len("hundred")
    thousand = len("thousand")
    and_word = len("and")
    
    def count_letters_below_100(n):
        if n < 10:
            return len(ones[n])
        elif n < 20:
            return len(teens[n - 10])
        else:
            return len(tens[n // 10 - 2]) + len(ones[n % 10])
    
    total_count = 0
    for i in range(1, n + 1):
        if i < 100:
            total_count += count_letters_below_100(i)
        elif i < 1000:
            total_count += len(ones[i // 100]) + hundred
            if i % 100 != 0:
                total_count += and_word + count_letters_below_100(i % 100)
        else:
            total_count += len(ones[1]) + thousand
    return total_count

print(count_letters(1000))
