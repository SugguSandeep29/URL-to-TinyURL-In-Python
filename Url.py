import pyshorteners 

link  = input("Enter The Url: ")

shortener = pyshorteners.Shortener()

x = shortener.tinyurl.short(link)

print(x)
