import requests
import re


if __name__ == '__main__':
    req = requests.get('http://www.columbia.edu/~fdc/sample.html')

    headline = re.findall(r'<{0}.*>(.*)</{0}>'.format('h3'), req.text)
    for x in headline:
        print(x)
    print(headline)
