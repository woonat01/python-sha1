#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sha1  # credit for sha1 from https://github.com/ajalt/python-sha1
import sys

print (sys.getdefaultencoding())

# message = input("What is your message?\n")
message = "comment1=Crypto%20Gurus;userdata=foo;comment2=%20hereAt%20UNO%20Omaha%20NE%20USA"
print("Message:\n" + message)

# key = input("What is your key?\n")
key = "A1852D554F5528A2A949FAC01087E6C9"
print("Key:\n" + key)

mac = bytes((key + message), 'utf-8')
# newline to accommodate the "echo" function specified in the original programs input.
# Don't use echo to test - it doesnt interpret the url well. Pass url in text file.
print("MAC: ")
print(mac)

origMac = sha1.sha1(mac)
# call sha1.py sha1 function and pass mac as input
print("sha1 digest original key + message: " + origMac)
# print("sha1 digest modified test  message: " + sha1.sha1Modified(mac))

# for SHA1 keyed MAC attack
newMessage = ";admin=true"
macAttack2 = bytes((newMessage + "\n"), 'utf-8')
# hashed with modified register
# extHash = sha1.sha1Modified(macAttack2)
# print("extHash:                            " + extHash)


keySize = len(key * 8)
print("keySize: " + str(keySize))
messageSize = len(message * 8)
print("messageSize: " + str(messageSize))

# length of mac in bits
macSize = len(mac * 8)
print("macSize: " + str(macSize))

# pad in bits - convert to bytes
pad = int((1024-(keySize+messageSize))/8)  # (macSize % 512)

print("Pad Size: " + str(pad))
# padding = start of padding + 0 padding * pad - leave length for beginning and length definition of pad
# must present hex as binary "b'x'"
# I have tried many combinations of pad lengths. Can't quite figure out what to put in as the pad.
padding = b'\x80' + (b'\x00' * (pad - 0)) + b'\x80'

previousMac = key + message

macAttack = bytes(previousMac, 'utf-8') + padding + bytes(newMessage, 'utf-8')
print("macAttack: " + str(macAttack))
newMac = sha1.sha1(macAttack)
print("newMac: " + str(newMac))


'''i = 1
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
'''