import time
import board
import digitalio
import adafruit_ssd1306
import psutil
import netifaces
import subprocess
from PIL import Image, ImageDraw, ImageFont

# Function to get the current IP address
def get_ip_address(interface='wlan0'):
    try:
        addresses = netifaces.ifaddresses(interface)
        ip = addresses[netifaces.AF_INET][0]['addr']
        return ip
    except:
        return "N/A"

# Function to get total CPU usage
def get_total_cpu_usage():
    return psutil.cpu_percent(interval=1)

# Function to get CPU temperature using vcgencmd
def get_cpu_temperature():
    try:
        cpu_temp_str = subprocess.check_output(['vcgencmd', 'measure_temp']).decode()
        cpu_temp = float(cpu_temp_str.split('=')[1].split('\'')[0])
        return cpu_temp
    except:
        return "N/A"

# Function to get memory usage
def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

# Function to get disk usage for the root filesystem
def get_disk_usage():
    partitions = psutil.disk_partitions(all=False)  # Exclude all virtual filesystems
    for partition in partitions:
        if partition.mountpoint == "/":
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                return (partition.device.split("/")[-1], usage.used, usage.percent)
            except:
                pass
    return None

def display_clock():
    # while True:
        # Get current time in 12-hour format without AM/PM
        current_time = time.strftime("%I:%M")

        # Create blank image
        image = Image.new("1", (oled.width, oled.height))

        # Calculate the size of the text and center it horizontally
        draw = ImageDraw.Draw(image)
        text_left, text_top, text_width, text_height = draw.textbbox((0,0),current_time, font=font)
        x = (WIDTH - text_width) // 2
        y = (HEIGHT - text_height) // 2

        # Draw the time on the image
        draw.text((x, y), current_time, font=font, fill="white")

        # Display the image on the OLED
        oled.image(image)
        oled.show()
        time.sleep(5)



# OLED display setup
reset_pin = digitalio.DigitalInOut(board.D4)
# OLED display setup
WIDTH = 128
HEIGHT = 64
I2C_ADDR = 0x3C
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=I2C_ADDR)

# Font size and style setup
FONT_SIZE = 64
font = ImageFont.truetype("/home/<user>/rpi4tower/7.ttf", FONT_SIZE)

# Clear the display once at the beginning
oled.fill(0)
oled.show()

# Load the bold and regular fonts for text
font_bold_10 = ImageFont.truetype("DejaVuSans-Bold.ttf", 10)
font_bold_14 = ImageFont.truetype("DejaVuSans-Bold.ttf", 14)

try:
    while True:
        # Create an image and draw object
        image = Image.new("1", (oled.width, oled.height))
        draw = ImageDraw.Draw(image)

        # Get and display the total CPU usage
        total_cpu_usage = get_total_cpu_usage()
        draw.text((0, 0), f"Total CPU: {total_cpu_usage:.1f}%", font=font_bold_10, fill=1)  # 1 for white color

        # Get and display the CPU temperature
        cpu_temp = get_cpu_temperature()
        if cpu_temp != "N/A":
            draw.text((0, 12), f"CPU Temp: {cpu_temp:.1f} \u00b0C", font=font_bold_10, fill=1)  # 1 for white color
        else:
            draw.text((0, 12), "CPU Temp: N/A", font=font_bold_10, fill=1)  # 1 for white color

        # Get and display the memory (RAM) usage
        memory_usage = get_memory_usage()
        draw.text((0, 24), f"MEM: {memory_usage:.1f}%", font=font_bold_10, fill=1)  # 1 for white color

        # Get and display the disk usage for the root filesystem
        disk_info = get_disk_usage()
        if disk_info is not None:
            drive_name, used, disk_usage = disk_info
            drive_text = f"{drive_name}: {used / (1024 ** 3):.1f}GB ({disk_usage:.1f}%)"
            draw.text((0, 36), drive_text, font=font_bold_10, fill=1)  # 1 for white color

        # Get and display the network IP at the bottom with a larger font
        ip_address = get_ip_address()
        ip_text_size = draw.textbbox((0,0),ip_address, font=font_bold_14)
        ip_x = (oled.width - ip_text_size[2]) // 2
        ip_y = oled.height - ip_text_size[3] - 1
        draw.text((ip_x, ip_y), ip_address, font=font_bold_14, fill=1)  # 1 for white color
        # Display the image on the OLED
        oled.image(image)
        oled.show()

        # Update every 5 seconds
        time.sleep(5)

        display_clock()

except KeyboardInterrupt:
    oled.fill(0)
    oled.show()
    #pass
