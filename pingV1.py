import os

hosts = True

IPs = []

while(hosts):
    user_input = input("Please enter the IP you would like to ping or type exit:\n")
    if (user_input != "exit"):
        IPs.append(user_input)
    else:
        hosts = False

# Create a for loop for each IP address to peform some action on it.
# if IP address gets pinged and returns a positive response print that.
# if IP does not return a positive response then print that.

for ip in IPs:
    response = os.system("ping -c 5 " + ip)
    
    if response == 0:
        print()
        print(f"{ip} is up")
        print()
    else:
        print()
        print(f"{ip} is down")
        print()
