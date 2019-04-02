# binstr = '01111111111111111111111111111111'
binstr = '11111111100000000000000000000000'
mantissa = 0.0
bias = 127

def binstring_to_decimal(binstr):
    if binstr[0] == '1':
        sign = -1
    else:
        sign = 1

    for bit in range(1, 8):
        if binstr[bit] == '0':
            break
        else:
            for bit in range(9, 32):
                if binstr[bit] == '1':
                    float_out = 'NaN'
                else:
                    float_out = 'Infinity'
            float_out = str(sign) + "*" + float_out
            return float_out

    exponent = int(binstr[2:9], 2)
    if binstr[1] == '0':
        exponent = exponent - bias
    else:
        exponent += 1

    for bit in range(31, 9, -1):
        if binstr[bit] == '1':
            break

    mantissa_string = binstr[9:bit+1]
    for bit in range(0, len(mantissa_string)):
        if mantissa_string[bit] == '1':
            mantissa = mantissa + (2 ** (-1 * (bit+1)))
    float_out = (sign*2**exponent*(1+mantissa))
    return float_out


print(binstring_to_decimal(binstr))