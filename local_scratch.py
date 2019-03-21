def binary_str_to_float(binary_string):
    sign = int(binary_string[0])
    exponent = 0
    mantissa = 0
    counter = 0

    for hold in range(31, 7, -1):
        if int(binary_string[hold]) == 1:
            mantissa = mantissa + (2 ** counter)
        counter += 1
    counter = 0
    if int(binary_string[1]) == 1:
        for hold in range(8, 2, -1):
            if int(binary_string[hold]) == 1:
                exponent = exponent + (2 ** counter)
            print(exponent)
            counter += 1
    else:
        for hold in range(8, 2, -1):
            if int(binary_string[hold]) == 1:
                exponent = exponent + (2 ** (-1 * counter))
            counter += 1
    if sign >= 0:
        return mantissa ** exponent
    else:
        return -1 * (mantissa ** exponent)

binary_string = '01111111011111111111111111111111'

print(binary_str_to_float(binary_string))
