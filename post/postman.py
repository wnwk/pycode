import requests
import json

urllist = ['http://url1', 'http://url2']

for i in urllist:
    r = requests.get(i)
    print('\n')
    print(
        json.dumps(
            json.loads(r.text), indent=4, sort_keys=False, ensure_ascii=False))
