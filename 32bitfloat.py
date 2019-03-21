from microbit import *

cursor_pos = 0
page = 1
BUTTON_HOLD = 2000


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


binary_string = '01111111011111111111111111111111'
page_1(binary_string, page)


def blink_cursor(cursor_pos):
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

    if int(display.get_pixel(x_axis, y_axis)) == 0:
        display.set_pixel(x_axis, y_axis, 9)
        sleep(200)
    else:
        display.set_pixel(x_axis, y_axis, 0)
        sleep(200)
    return cursor_pos


def binary_str_to_float(binary_string):
    sign = int(binary_string[0])
    exponent = 0
    mantissa = 0
    counter = 0

    for hold in range(31, 7, -1):
        if binary_string[hold] == 1:
            mantissa = mantissa + (2 ** counter)
        counter += 1
    counter = 0
    if binary_string[1] == 1:
        for hold in range(8, 2, -1):
            if binary_string[hold] == 0:
                exponent = exponent + (2 ** counter)
            counter += 1
    else:
        for hold in range(8, 2, -1):
            if binary_string[hold] == 1:
                exponent = exponent + (2 ** (-1 * counter))
            counter += 1
    if sign >= 0:
        return mantissa ** exponent
    else:
        return -1 * (mantissa ** exponent)


while True:
    curtime = running_time()
    cursor_pos = blink_cursor(cursor_pos)
    pressed_time = 0
    while button_b.is_pressed():
        pressed_time = running_time() - curtime
    if int(cursor_pos) < 24 and pressed_time < BUTTON_HOLD and pressed_time > 0:
        page = page_1(binary_string, page)
        cursor_pos += 1
    elif int(cursor_pos) < 31 and pressed_time < BUTTON_HOLD and pressed_time > 0:
        page = page_2(binary_string, page)
        cursor_pos += 1
    elif int(cursor_pos) > 30 and pressed_time < BUTTON_HOLD and pressed_time > 0:
        display.clear()
        page = 2
        cursor_pos = 0
        page_1(binary_string, page)
    elif pressed_time > BUTTON_HOLD:
        display.scroll("Menu")
        if page == 1:
            page = page_1(binary_string, page)
        else:
            page = page_2(binary_string, page)
    if button_a.is_pressed():
        if binary_string[cursor_pos] == '0':
            binary_string = binary_string[:cursor_pos] + '1' + binary_string[cursor_pos + 1:]
        else:
            binary_string = binary_string[:cursor_pos] + '0' + binary_string[cursor_pos + 1:]
    elif pin0.is_touched():
        display.scroll(binary_str_to_float(binary_string))
        if page == 1:
            page = page_1(binary_string, page)
        else:
            page = page_2(binary_string, page)

