#!/usr/bin/env python
import sha1  # credit for sha1 from https://github.com/ajalt/python-sha1

# message = input("What is your message?\n")
message = "comment1=Crypto%20Gurus;userdata=foo;comment2=%20hereAt%20UNO%20Omaha%20NE%20USA"
print("Message: " + message)

# key = input("What is your key?\n")
key = "A1852D554F5528A2A949FAC01087E6C9"
print("Key: " + key)

mac = bytes((key + message + "\n"), 'utf-8')  # newline to accommodate the "echo" function specified in the original
# programs input. Don't use echo to test - it doesnt interpret the url well. Pass url in text file
# mac = bytes((message + "\n"), 'utf-8')  # to test if key was working
print("MAC: ")
print(mac)
print()

# call sha1.py sha1 function and pass mac as input
print("sha1 digest original key + URL: " + sha1.sha1(mac))

# for SHA1 keyed MAC attack
newMessage = ";admin=true"


