import re


def sanitize(url):
    clean = url.replace(' ', '_')
    clean = re.sub("[^a-zA-Z0-9-_]", "", clean)
    print(clean)