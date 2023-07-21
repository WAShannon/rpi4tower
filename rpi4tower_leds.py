import board
import neopixel
import time

# LED strip configuration
LED_COUNT = 4           # Number of LED pixels
LED_PIN = board.D18     # GPIO pin connected to the LED strip (GPIO18)
LED_BRIGHTNESS = 0.2    # Brightness (0.0 to 1.0)
LED_ORDER = neopixel.GRB  # Strip color order (GRB for WS2812B)

# Initialize the LED strip
strip = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)

def set_led_color(index, r, g, b):
    """Set the color of the LED at the given index."""
    strip[index] = (r, g, b)
    strip.show()

def turn_off_leds():
    """Turn off all LEDs."""
    for i in range(LED_COUNT):
        set_led_color(i, 0, 0, 0)

# Example usage
if __name__ == "__main__":
    try:
        # Set individual LED colors
        set_led_color(0, 255, 0, 0)  # Red
        set_led_color(1, 0, 255, 0)  # Green
        set_led_color(2, 0, 0, 255)  # Blue
        set_led_color(3, 255, 255, 0)  # Yellow

        # Wait for a few seconds
        time.sleep(5)

        # Turn off all LEDs
        turn_off_leds()

    except KeyboardInterrupt:
        # Turn off LEDs and handle keyboard interrupt
        turn_off_leds()
