# pip3 install pywhatkit
import pywhatkit
text = '''
Let’s say you are working on a project that needs to do web scraping but
you don’t know websites on which scraping is to be performed beforehand 
instead you are required to perform a google search and then proceed according 
to google search results to a few websites. In that case, you need google search 
results for your different queries.
'''

pywhatkit.text_to_handwriting(text, save_to="handwriting.png")
