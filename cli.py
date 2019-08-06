import sys
import json
import argparse

from goop import goop

parser = argparse.ArgumentParser(description='Process user information')
parser.add_argument('--query', '-q', type=str, help='Query parameter', required=True)
parser.add_argument('--cookie', type=str, help='Facebook cookie')

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--pages', '-P', type=int, help='Total page count')
group.add_argument('--page', '-p', type=int, help='Page index for retrieval')
group.add_argument('--range', '-r', type=int, help='Range of page index', nargs=2)
group.add_argument('--count', '-c', type=int, help='Total entries count')

args = parser.parse_args()

page = args.page
custom_range = args.range
pages = args.pages
count = args.count
query = args.query

green = '\033[92m'
white = '\033[97m'
yellow = '\033[93m'
end = '\033[0m'

cookie = args.cookie or None #'<your facebook cookie>'
if not cookie:
    raise Exception("Add facebook cookie to use goop")

if count:
    pages = range(count)
elif pages:
    pages = range(pages)
elif page:
    pages = range(page, page+1)
elif custom_range:
    start, end = custom_range
    pages = range(start, end)

for page in pages:
    result = goop.search(query, cookie, page=page, full=True, count=count)

    for each in result:
	print ('''%s%s\n%s%s\n%s%s%s\n''' % (green, result[each]['text'], yellow, result[each]['url'], white, result[each]['summary'], end))

    if count:
        count = count - len(result)
        if count <= 0:
            break
