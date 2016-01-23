import urllib

def read_test():
    quotes = open("movie_quotes.txt")
    contents_of_file = quotes.read()
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print "Profanity Alert!"
    elif "false" in output:
        print "This document has no curse words!"
