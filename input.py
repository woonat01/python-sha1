#!/usr/bin/env python
import sha1  # credit for project from https://github.com/ajalt/python-sha1

message = input("What is your message?\n")
print(message)

key = input("What is your key?\n")
print(key)

mac = bytes((key + message + "\n"), 'utf-8')  # newline to accommodate the "echo" function specified in the original
# programs input.

print(mac)

print("sha1 digest: " + sha1.sha1(mac))
