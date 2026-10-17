from devices import devices
# Network Explorer — Level 1
# Mission 1: Create a network device

# TODO: Create a dictionary named pc1
# Add hostname, ip_address, subnet_mask,
# device_type, and status.


print(devices["pc1"]["hostname"],
      devices["pc1"]["ip_address"],
      devices["pc1"]["device_type"],
      sep="\n"
      )



#iteration of devices in pc1
print("===DEVICE INFORMATION===")

for key, value in devices["pc1"].items():
    print(f"{key}: {value}")
