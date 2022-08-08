import webbrowser

std = input("Enter the string: ")
url = "https://pywhatkit.herokuapp.com/handwriting?text="
text = url + std
webbrowser.open_new(text)