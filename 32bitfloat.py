from microbit import *

cursor_pos = 0
page = 1


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


while True:
    cursor_pos = blink_cursor(cursor_pos)
    if button_b.is_pressed() and int(cursor_pos) < 24:
        page = page_1(binary_string, page)
        cursor_pos += 1
    elif button_b.is_pressed() and int(cursor_pos) < 31:
        page = page_2(binary_string, page)
        cursor_pos += 1
    elif button_b.is_pressed() and int(cursor_pos) > 30:
        display.clear()
        page = 2
        cursor_pos = 0
        page_1(binary_string, page)
    elif button_a.is_pressed():
        if binary_string[cursor_pos] == '0':
            binary_string = binary_string[:cursor_pos] + '1' + binary_string[cursor_pos + 1:]
        else:
            binary_string = binary_string[:cursor_pos] + '0' + binary_string[cursor_pos + 1:]

