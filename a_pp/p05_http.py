"""
CSE 2110: Procedural Programming
Exception Handling

"""

from urllib.request import urlopen

def main():
    url = input("Enter a URL: ")
    data = urlopen(url).read()
    print(data)

main()
