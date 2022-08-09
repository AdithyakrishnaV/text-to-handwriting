import requests


def write():
    std = input("Enter the string: ")
    url = "https://pywhatkit.herokuapp.com/handwriting?text="
    search = url + std

    status = requests.get(
        search
    )
    # download 
    open('writing.png', 'wb').write(status.content) #pyhton file handling


write()
