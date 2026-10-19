def ping_device (ip_address, status):
        print(f"Pinging : {ip_address}")
        if status == "Online":
            print("Reply recieved")
        else: 
            print ("No reply")
        
