binary = ""
basic.clear_screen()

while True:
    if input.button_is_pressed(Button.A):
        binary += "0"
        basic.show_number(0)
        basic.pause(100)
        basic.clear_screen()
    elif input.button_is_pressed(Button.B):
        binary += "1"
        basic.show_number(1)
        basic.pause(100)
        basic.clear_screen()

    if len(binary) == 4:
        decimal = int(binary,2)
        basic.show_number(decimal)
        binary = ""
        basic.pause(500)
        basic.clear_screen()

#adapt this program to create a quiz which displays a number decimal between 0 and 15
#allows the user to enter it in binary and displays a tick or a cross to show if they are correct
#you can use basic.show_icon(IconNames.YES) and basic.show_icon(IconNames.NO) for the tick and cross