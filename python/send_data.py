import requests
import random
import time

WRITE_API_KEY = "BBDVV7NU8DMRS8PG"

while True:
    voltage = random.randint(220, 240)
    current = round(random.uniform(1.0, 5.0), 2)
    power = round(voltage * current, 2)
    energy = round(power / 1000, 2)
    temperature = random.randint(25, 40)
    device = 1

    url = "https://api.thingspeak.com/update"

    data = {
        "api_key": WRITE_API_KEY,
        "field1": voltage,
        "field2": current,
        "field3": power,
        "field4": energy,
        "field5": temperature,
        "field6": device
    }

    response = requests.post(url, data=data)

    print("=" * 40)
    print("Data Uploaded Successfully")
    print(f"Voltage: {voltage} V")
    print(f"Current: {current} A")
    print(f"Power: {power} W")
    print(f"Energy: {energy} kWh")
    print(f"Temperature: {temperature} °C")
    print(f"ThingSpeak Response: {response.text}")

    time.sleep(20)