from microbit import *


# For Page 1
def page_1(binary_string):
    for ctr in range(1, 26):
        led_status = binary_string[int(ctr - 1)]
        y_axis = int(ctr - 1) // 5
        x_axis = int(ctr - 1) % 5
        if int(led_status) == int(1):
            bin_value = 9
        else:
            bin_value = 0

        print("Position number "+str(ctr)+": ("+str(x_axis)+", "+str(y_axis)+", "+str(bin_value)+")")
        display.set_pixel(x_axis, y_axis, bin_value)


# For Page 2
def page_2(binary_string):
    for ctr in range(27, 32):
        led_status = binary_string[int(ctr - 1)]
        y_axis = (int(ctr - 1) // 5) - 5
        x_axis = int(ctr - 1) % 5
        print("Position number "+str(ctr)+": ("+str(x_axis)+", "+str(y_axis)+", 9)")


binary_string = '01111111011111111111111111111111'
print(page_1(binary_string))
cursor_pos = 0
page = 1


def blink_cursor(cursor_pos, page):
    x_axis = cursor_pos % 5
    y_axis = cursor_pos // 5
    if int(display.get_pixel(x_axis, y_axis)) == 0:
        display.set_pixel(x_axis, y_axis, 9)
        sleep(150)
    else:
        display.set_pixel(x_axis, y_axis, 0)
        sleep(150)


while True:
    blink_cursor(cursor_pos, page)
    if button_b.is_pressed() and cursor_pos < 26:
        page_1(binary_string)
        cursor_pos += 1

