import time
import board
import digitalio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# OLED display setup
WIDTH = 128
HEIGHT = 64
I2C_ADDR = 0x3C
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=I2C_ADDR)

# Font size and style setup
FONT_SIZE = 64
font = ImageFont.truetype("7.ttf", FONT_SIZE)

def display_clock():
    # while True:
        # Get current time in 12-hour format without AM/PM
        current_time = time.strftime("%I:%M")

        # Create blank image
        image = Image.new("1", (oled.width, oled.height))

        # Calculate the size of the text and center it horizontally
        draw = ImageDraw.Draw(image)
        text_width, text_height = draw.textsize(current_time, font=font)
        x = (WIDTH - text_width) // 2
        y = (HEIGHT - text_height) // 2

        # Draw the time on the image
        draw.text((x, y), current_time, font=font, fill="white")

        # Display the image on the OLED
        oled.image(image)
        oled.show()

        # Scroll off the bottom after 5 seconds
        time.sleep(5)

        # Scroll the image off the bottom of the screen (even faster scrolling)
        for i in range(HEIGHT):
            oled.scroll(0, -1)
            oled.show()
            time.sleep(0.001)  # Adjust this value to control scrolling speed

if __name__ == "__main__":
    try:
        display_clock()
    except KeyboardInterrupt:
        # Clear the display on exit
        oled.fill(0)
        oled.show()
