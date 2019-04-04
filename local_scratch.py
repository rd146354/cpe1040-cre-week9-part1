# binstr = '01111111111111111111111111111111'
binstr = '01111111011111111111111111111111'



def binstring_to_decimal(binstr):
    mantissa = 0.0
    bias = 127
    if binstr[0] == '1':
        sign = -1
    else:
        sign = 1

    exponent = int(binstr[1:9], 2)
    exponent -= bias
    for bit in range(31, 9, -1):
        if binstr[bit] == '1':
            break
    mantissa_string = binstr[9:bit+1]
    for bit in range(0, len(mantissa_string)):
        if mantissa_string[bit] == '1':
            mantissa = mantissa + (2 ** (-1 * (bit+1)))
    float_out = (sign*2**exponent*(1+mantissa))
    return float_out


def binstring_to_signed(binstr):
    signed_int = int(binstr[1:], 2)
    if binstr[0] == '1':
        signed_int = signed_int * (-1)
    print(signed_int)

def binstring_to_chars(binstr):
    asciistring = chr(int(binstr[0:7], 2)) \
        + chr(int(binstr[8:15], 2)) \
        + chr(int(binstr[16:23], 2)) \
        + chr(int(binstr[24:31], 2))
    print(int(binstr[0:7], 2))
    print(int(binstr[8:15], 2))
    print(int(binstr[16:23], 2))
    print(int(binstr[24:31], 2))
    print(asciistring)


binstring_to_signed(binstr)
print(binstring_to_decimal(binstr))
binstring_to_chars(binstr)