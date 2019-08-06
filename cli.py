import sys
import json
import argparse

from goop import goop

parser = argparse.ArgumentParser(description='Process user information')
parser.add_argument('--query', '-q', type=str, help='Query parameter', required=True)

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--pages', '-P', type=int, help='Total page count')
group.add_argument('--count', '-c', type=int, help='Total entries count')

args = parser.parse_args()
pages = args.pages or 1
count = args.count
query = args.query

green = '\033[92m'
white = '\033[97m'
yellow = '\033[93m'
end = '\033[0m'

#cookie = '<your facebook cookie>'
cookie ="sb=boLvXDSrzYhVnIKWXOFFW041; datr=boLvXPKbLlyVoB80_a3jBYga; c_user=100001279151010; xs=81%3AsekDgdXtTHvMpg%3A2%3A1559200373%3A9277%3A4202; dpr=1.125; ; spin=r.1001023063_b.trunk_t.1565064737_s.1_v.2_; fr=04L1QWkX5tO2cXBfm.AWUZ47IHTKAlNM_-5JktDQIYrxE.Bc7meN.yw.F1G.0.0.BdSP4i.AWUFvl3v; wd=1091x838; presence=EDvF3EtimeF1565064744EuserFA21B01279151010A2EstateFDutF1565064744973CEchFDp_5f1B01279151010F1CC"

if count:
    pages = count

for page in range(pages):
    result = goop.search(query, cookie, page=page, full=True, count=count)

    for each in result:
	print ('''%s%s\n%s%s\n%s%s%s\n''' % (green, result[each]['text'], yellow, result[each]['url'], white, result[each]['summary'], end))

    if count:
        count = count - len(result)
        if count <= 0:
            break
