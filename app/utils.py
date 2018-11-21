import re


# Sanitize tournament name
def sanitize(url):
    clean = url.replace(' ', '_')
    clean = re.sub("[^a-zA-Z0-9-_]", "", clean)
    return clean