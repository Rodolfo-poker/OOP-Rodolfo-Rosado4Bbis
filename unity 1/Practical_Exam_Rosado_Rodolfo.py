class Servers:
    def __init__(self, hostname, ip_address, ram, status):
        self.hostname = hostname
        self.ip_address = ip_address
        self.ram = ram
        self.status = status
    
    def show_server_info(self):
        if self.status == True:
            status_server = "ACTIVE"
        else:
            status_server = "INACTIVE" 
        print(f"Hostname: {self.hostname} \n IP Address: {self.ip_address} \n RAM memory capacity: {self.ram} GB \n Status: {status_server}")
    
    def power_on_server(self):
        if self.status == False:
            print(f"The server {self.hostname} is now actived \n The status changed to ACTIVE")
            self.status = True
        elif self.status == True:
            print(f"The server is already on...")
        else:
            print("The server could NOT be found, please check hostname...")
    
    def power_off_server(self):
        if self.status == True:
            print(f"The server {self.hostname} is now inactivated \n The status changed to INACTIVE")
            self.status = False
        elif self.status == False:
            print(f"The server is already off...")
        else:
            print("The server could NOT be found, please check hostname...")
    
    def update_ram(self):
        new_ram = float(input("How much RAM will the server get? (Introduce a number in GB):"))
        if new_ram <= 0:
            print("You have to introduce a number higher than 0 ")
        elif new_ram >= 0:
            self.ram += new_ram
            print(f"The RAM capacity of the server has been updated to {self.ram}")
        else:
            print("You have to introduce only numbers...")
        
class Data_centers:
    def __init__(self, region):
        self.region = region
        self.servers = []
    
    def register_server(self, server):
        self.servers.append(server)
        print(f"Server {server.hostname} registered in {self.region} data center")
    
    def show_active_servers(self):
        active_servers = [server.hostname for server in self.servers if server.status == True]
        print(f"\nActive servers in {self.region} data center:")
        if active_servers:
            for hostname in active_servers:
                print(f"{hostname}")
        else:
            print("No active servers")

data_center1 = Data_centers("Mexico - North")
server1 = Servers("web-server-01", "192.168.1.10", 16, True)
server2 = Servers("db-server-01", "192.168.1.20", 32, False)

server1.show_server_info()

server2.power_on_server()
server1.power_off_server()

server2.update_ram()

data_center1.register_server(server2)

data_center1.show_active_servers()