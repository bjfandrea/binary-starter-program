let decimal: number;
let binary = ""
basic.clearScreen()
while (true) {
    if (input.buttonIsPressed(Button.A)) {
        binary += "0"
        basic.showNumber(0)
        basic.pause(100)
        basic.clearScreen()
    } else if (input.buttonIsPressed(Button.B)) {
        binary += "1"
        basic.showNumber(1)
        basic.pause(100)
        basic.clearScreen()
    }
    
    if (binary.length == 4) {
        decimal = parseInt(binary, 2)
        basic.showNumber(decimal)
        binary = ""
        basic.pause(500)
        basic.clearScreen()
    }
    
}
