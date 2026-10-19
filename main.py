from devices import devices
from network import ping_device
# Network Explorer — Level 1
# Mission 1: Create a network device

# TODO: Create a dictionary named pc1
# Add hostname, ip_address, subnet_mask,
# device_type, and status.


# print(devices["pc1"]["hostname"],
#       devices["pc1"]["ip_address"],
#       devices["pc1"]["device_type"],
#       sep="\n"
#       )



#iteration of devices in pc1
# print("===DEVICE INFORMATION===")

# for key, value in devices["pc1"].items():
#     print(f"{key}: {value}")

# for number, (device_id, device_info) in enumerate(devices.items(), start=1):
#     print(f"{device_info['hostname']} : {device_info['ip_address']}"),

# print(len(devices)) 

ping_device(devices["pc2"]["ip_address"],devices["pc2"]["status"])