#!/usr/bin/env python
import sha1  # credit for sha1 from https://github.com/ajalt/python-sha1
import struct
# message = input("What is your message?\n")
message = "comment1=Crypto%20Gurus;userdata=foo;comment2=%20hereAt%20UNO%20Omaha%20NE%20USA"
print("Message:\n" + message)

# key = input("What is your key?\n")
key = "A1852D554F5528A2A949FAC01087E6C9"
print("Key:\n" + key)

mac = bytes((key + message + "\n"), 'utf-8')
# newline to accommodate the "echo" function specified in the original programs input.
# Don't use echo to test - it doesnt interpret the url well. Pass url in text file.
print("MAC: ")
print(mac)
print()

origMac = sha1.sha1(mac)
# call sha1.py sha1 function and pass mac as input
print("sha1 digest original key + message: " + origMac)
# print("sha1 digest modified test  message: " + sha1.sha1Modified(mac))

# for SHA1 keyed MAC attack
newMessage = ";admin=true"
macAttack2 = bytes((newMessage + "\n"), 'utf-8')
# hashed with modified register
extHash = sha1.sha1Modified(macAttack2)
print("extHash:                            " + extHash)


keySize = len(key + "\n")
print("keySize: " + str(keySize))
messageSize = len(message)
print("messageSize: " + str(messageSize))
macSize = len(mac)
print("macSize: " + str(macSize))
i = 1
for i in range (0, 512):

    pad = i  # (macSize % 64)
    print("Pad Size: " + str(pad))

    padding = '\x80' + '\x00' * pad

    macAttack = bytes((key + message + "\n" + padding + newMessage), 'utf-8')
    #macAttack = bytes((newMessage + padding + "\n" ), 'utf-8')

    newMac = sha1.sha1(macAttack)
    print("sha1 digest original key + message: " + sha1.sha1(mac))
    #print("macAttack: " + str(macAttack))
    print("newMac: " + str(newMac))
    if newMac == origMac:
        print("SUCCESS")
        break
    i += 1




