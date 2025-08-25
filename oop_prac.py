# def __init__(self, name, ip_address):
#    ↑      ↑     ↑        ↑
#    │      │     │        └─ Parameter 2
#    │      │     └─ Parameter 1  
#    │      └─ Always first parameter (refers to "this object")
#    └─ Special method name (constructor)

# When you do: web_server = Server("web-01", "192.168.1.10")
# Python automatically calls: __init__(web_server, "web-01", "192.168.1.10")

class Server:
    def __init__(self, name: str, ip_address: str):
        self.name = name
        self.ip_address = ip_address
        self.status = "Stopped"
        self.uptime_days = 0

# create an object using that class
web_server = Server(name="Cutiepie", ip_address="192.168.1.10")

print(f"Server name: {web_server.name}")
print(f"Server ip_address: {web_server.ip_address}")
print(f"Server status: {web_server.status}")
print(f"Server uptime_days: {web_server.uptime_days}")

# Adding Methods (Actions): to the class

class Server2:
    def __init__(self, name: str, ip_address: str):
        self.name = name
        self.ip_address = ip_address
        self.status = "Stopped"
        self.uptime_days = 0

    def start(self):
        if self.status == "Stopped":
            self.status = "Running"
            print(f" {self.name} is now running!")
        else:
            print(f"DANGER fail to start {self.name}")

web_server = Server2("nginx", "192.168.1.10")
print(f"Server2 status now: {web_server.status}")
print("Starting webster using: web_server.start()")
web_server.start() #this will execute the class in the def