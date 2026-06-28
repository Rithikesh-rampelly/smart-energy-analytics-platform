import random

# List of devices in the building
devices = [
    {"name": "Air Conditioner", "voltage": 230, "current": round(random.uniform(3.5, 5.0), 2)},
    {"name": "Lights", "voltage": 230, "current": round(random.uniform(0.8, 1.5), 2)},
    {"name": "Ceiling Fan", "voltage": 230, "current": round(random.uniform(0.5, 1.0), 2)},
    {"name": "Water Pump", "voltage": 230, "current": round(random.uniform(4.0, 6.0), 2)}
]

print("=" * 60)
print("SMART BUILDING ENERGY SIMULATION")
print("=" * 60)

total_power = 0

for device in devices:
    power = device["voltage"] * device["current"]
    total_power += power

    print(f"\nDevice      : {device['name']}")
    print(f"Voltage     : {device['voltage']} V")
    print(f"Current     : {device['current']} A")
    print(f"Power       : {round(power,2)} W")

print("\n" + "=" * 60)
print(f"Total Building Power : {round(total_power,2)} W")
print("=" * 60)