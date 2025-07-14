import RPi.GPIO as GPIO
import time

# Use BCM pin numbering
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def get_disk_activity():
    with open("/proc/diskstats", "r") as f:
        for line in f:
            if "mmcblk0" in line:
                fields = line.split()
                # Field 6 = # of reads completed
                # Field 10 = # of writes completed
                reads = int(fields[3])
                writes = int(fields[7])
                return reads, writes
    return 0, 0

last_reads, last_writes = get_disk_activity()

try:
    while True:
        time.sleep(0.1)  # 100 ms interval
        reads, writes = get_disk_activity()

        if reads != last_reads or writes != last_writes:
            GPIO.output(LED_PIN, GPIO.HIGH)  # ON when activity
            time.sleep(0.05)
            GPIO.output(LED_PIN, GPIO.LOW)   # Blink off
        else:
            GPIO.output(LED_PIN, GPIO.LOW)

        last_reads, last_writes = reads, writes

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
