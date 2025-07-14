import asyncio
from bleak import BleakClient

HM10_MAC = "20:91:48:XX:XX:XX"  # Replace with your HM-10 MAC
UART_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

async def run():
    async with BleakClient(HM10_MAC) as client:
        print("Connected:", await client.is_connected())

        def notification_handler(_, data):
            print("Arduino says:", data.decode(errors='ignore'))

        # Subscribe to notifications (incoming data)
        await client.start_notify(UART_UUID, notification_handler)

        # Send a message
        message = "Hello from Pi!\n"
        await client.write_gatt_char(UART_UUID, message.encode())

        # Wait to receive response
        await asyncio.sleep(5)

        # Unsubscribe
        await client.stop_notify(UART_UUID)

asyncio.run(run())
