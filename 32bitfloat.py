from microbit import *

cursor_pos = 0
page = 1
BUTTON_HOLD = 2000
binary_string = '01111111011111111111111111111111'


# For Page 1
def page_1(binary_string, page):
    if page == 2:
        display.clear()
        page = 1

    for ctr in range(1, 26):
        led_status = binary_string[int(ctr - 1)]
        y_axis = int(ctr - 1) // 5
        x_axis = int(ctr - 1) % 5
        if int(led_status) == int(1):
            bin_value = 9
        else:
            bin_value = 0

        # print("Position number "+str(ctr)+": ("+str(x_axis)+", "+str(y_axis)+", "+str(bin_value)+")")
        display.set_pixel(x_axis, y_axis, bin_value)
    return page


# For Page 2
def page_2(binary_string, page):
    if page == 1:
        display.clear()
        page = 2

    for ctr in range(26, 33):
        led_status = binary_string[int(ctr - 1)]
        y_axis = (int(ctr - 1) // 5) - 5
        x_axis = int(ctr - 1) % 5
        if int(led_status) == int(1):
            bin_value = 9
        else:
            bin_value = 0

        display.set_pixel(x_axis, y_axis, bin_value)
        # print("Position number "+str(ctr)+": ("+str(x_axis)+", "+str(y_axis)+", "+str(bin_value)+")")
    return page


# Function changes cursor status
def blink_cursor(cursor_pos):
    sleep_delay = 200
    curtime = int(running_time())

    if int(cursor_pos) < 25:
        x_axis = cursor_pos % 5
        y_axis = cursor_pos // 5
    elif int(cursor_pos) > 31:
        cursor_pos = 0
        x_axis = cursor_pos % 5
        y_axis = cursor_pos // 5
    else:
        x_axis = cursor_pos % 5
        y_axis = (cursor_pos // 5) - 5
    while int(running_time()) < (curtime + sleep_delay):
        if int(display.get_pixel(x_axis, y_axis)) == 0 and int(running_time()) < (curtime + 5):
            display.set_pixel(x_axis, y_axis, 9)
        elif int(running_time()) < (curtime + 5):
            display.set_pixel(x_axis, y_axis, 0)
        sleep(5)
        if button_a.is_pressed() or button_b.is_pressed():
            return cursor_pos
    return cursor_pos


# Convert the binary string to float
def binstring_to_decimal(binstr):
    mantissa = 0.0
    bias = 127
    if binstr[0] == '1':
        sign = -1
    else:
        sign = 1

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


# Caller for conversions
def convert_value(binary_string, position):
    if position == 0:
        display.scroll(int(binary_string, 2))
    elif position == 1:
        int_signed = int(binary_string[1:], 2)
        if binary_string[0] == '1':
            int_signed = int_signed * (-1)
        display.scroll(int_signed)
    elif position == 2:
        display.scroll(binstring_to_decimal(binary_string))
    else:
        characters = []
        bitposless1 = 0
        for bitpos in range(7, 39, 8):
            characters.append(binary_string[bitposless1:bitpos])
            bitposless1 = bitpos + 1
        display.scroll('String of 4 ASCII Characters')


# Menu screen
def menu(binary_string, BUTTON_HOLD):
    options = ['U', 'I', 'F', 'C']
    position = int(0)
    while True:
        display.show(str(options[position]))
        curtime = running_time()
        pressed_time = 0
        while button_b.is_pressed():
            pressed_time = running_time() - curtime
        if 0 < pressed_time < BUTTON_HOLD:
            sleep(100)
            convert_value(binary_string, position)
        elif pressed_time > BUTTON_HOLD:
            break
        pressed_time = 0
        while button_a.is_pressed():
            pressed_time = running_time() - curtime
        if 0 < pressed_time < BUTTON_HOLD:
            sleep(150)
            if position < 3:
                position += 1
            else:
                position = 0


# Initialize the screen
page_1(binary_string, page)
# Main program loop
while True:
    curtime = running_time()
    cursor_pos = blink_cursor(cursor_pos)
    pressed_time = 0
    while button_b.is_pressed():
        pressed_time = running_time() - curtime
    if int(cursor_pos) < 24 and 0 < pressed_time < BUTTON_HOLD:
        page = page_1(binary_string, page)
        cursor_pos += 1
    elif int(cursor_pos) < 31 and 0 < pressed_time < BUTTON_HOLD:
        page = page_2(binary_string, page)
        cursor_pos += 1
    elif int(cursor_pos) > 30 and 0 < pressed_time < BUTTON_HOLD:
        display.clear()
        page = 2
        cursor_pos = 0
        page_1(binary_string, page)
    elif pressed_time > BUTTON_HOLD:
        menu(binary_string, BUTTON_HOLD)
        if page == 1:
            page = page_1(binary_string, page)
        else:
            page = page_2(binary_string, page)
    if button_a.is_pressed():
        if binary_string[cursor_pos] == '0':
            binary_string = binary_string[:cursor_pos] + '1' + binary_string[cursor_pos + 1:]
        else:
            binary_string = binary_string[:cursor_pos] + '0' + binary_string[cursor_pos + 1:]
        sleep(300)
