import pyshorteners

a = pyshorteners.Shortener()

url = ("Enter the complete url you want to short:\n")

print(a.tinyurl.short(url))
