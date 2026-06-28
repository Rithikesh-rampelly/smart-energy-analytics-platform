import random
import requests
import time
import csv
import os

WRITE_API_KEY = "BBDVV7NU8DMRS8PG"

# Automatically find the project folder
current_folder = os.path.dirname(__file__)
project_folder = os.path.dirname(current_folder)
data_folder = os.path.join(project_folder, "data")

# Create the data folder if it doesn't exist
os.makedirs(data_folder, exist_ok=True)

# CSV file path
file_path = os.path.join(data_folder, "energy_data.csv")

while True:

    # Smart Building Devices
    devices = [
        {"name": "Air Conditioner", "voltage": 230, "current": round(random.uniform(3.5, 5.0), 2)},
        {"name": "Lights", "voltage": 230, "current": round(random.uniform(0.8, 1.5), 2)},
        {"name": "Ceiling Fan", "voltage": 230, "current": round(random.uniform(0.5, 1.0), 2)},
        {"name": "Water Pump", "voltage": 230, "current": round(random.uniform(4.0, 6.0), 2)}
    ]

    total_power = 0

    print("\n" + "=" * 60)
    print("SMART BUILDING LIVE MONITOR")
    print("=" * 60)

    for device in devices:
        power = device["voltage"] * device["current"]
        total_power += power

        print(f"{device['name']:<20} {round(power,2)} W")

    average_voltage = 230
    average_current = round(
        sum(device["current"] for device in devices) / len(devices),
        2
    )
    energy = round(total_power / 1000, 2)
    temperature = random.randint(25, 40)

    # ThingSpeak Data
    url = "https://api.thingspeak.com/update"

    data = {
        "api_key": WRITE_API_KEY,
        "field1": average_voltage,
        "field2": average_current,
        "field3": round(total_power, 2),
        "field4": energy,
        "field5": temperature,
        "field6": len(devices)
    }

    # Save to CSV
    file_exists = os.path.isfile(file_path)

    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(file_path) == 0:
            writer.writerow([
                "Voltage",
                "Average Current",
                "Total Power",
                "Energy",
                "Temperature",
                "Devices"
            ])

        writer.writerow([
            average_voltage,
            average_current,
            round(total_power, 2),
            energy,
            temperature,
            len(devices)
        ])

    # Upload to ThingSpeak
    response = requests.post(url, data=data)

    print("\n----------------------------------------")
    print("Cloud Upload Status")
    print("----------------------------------------")
    print(f"Average Voltage : {average_voltage} V")
    print(f"Average Current : {average_current} A")
    print(f"Total Power     : {round(total_power,2)} W")
    print(f"Energy          : {energy} kWh")
    print(f"Temperature     : {temperature} C")
    print(f"Devices         : {len(devices)}")
    print(f"ThingSpeak Response : {response.text}")

    print("\nData saved to:")
    print(file_path)

    print("\nWaiting 20 seconds for next upload...\n")

    time.sleep(20)