import subprocess

interface = input("Enter the interface name:- ")

new_mac = "00.55.66.99.77.55"

print("changing the new mac address")

subprocess.call(['ifconfig',interface,'down'])
subprocess.call(['ifconfig',interface,'hw','wlan0',new_mac])
subprocess.call(['ifconfig', interface,'up'])

print(" mac address has been changed...")
