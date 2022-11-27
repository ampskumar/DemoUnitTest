# import requests module
import requests
from datetime import datetime, timedelta

dev = 'd-delivery-api.movetv.com'
qa = 'q-delivery-api.movetv.com'
beta = 'b-delivery-api.movetv.com'

api = ['/live', '/ready', '/cc/summary' , '/cc/channels']

for x in api:
    d = 'http://' + dev + x
    q = 'http://' + qa + x
    b = 'http://' + beta + x

    # print(d)
    # print(q)
    # print(b)

    dr = timedelta(0)
    qr = timedelta(0)
    br = timedelta(0)
   
    for y in range(0,20):
        response_dev = requests.get(d)
        response_qa = requests.get(q)
        response_beta = requests.get(b)

        print(response_dev.elapsed)
        print(response_qa.elapsed)
        print(response_beta.elapsed)
        
# Total timing addition
        dr += response_dev.elapsed
        qr += response_qa.elapsed
        br += response_beta.elapsed

    # print(dr)
    # print(qr)
    # print(br)

    # Mean timing
    dr = dr / 20
    qr = qr / 20
    br = br /20

   
    print(f'Response time of {d} is {dr}')
    # print(f'Response content of {d} is {response_dev.text}')

    
    print(f'Response time of {q} is {qr}')
    # print(f'Response content of {q} is {response_qa.text}')

    
    print(f'Response time of {b} is {br}')
    # print(f'Response content of {b} is {response_beta.text}')



