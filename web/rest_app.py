'''

@author: xyj
'''

import requests
import json

#===============================================================================
# post_cdr : call REST API post cdr record
#===============================================================================
def post_cdr(url, payload) :
    response = requests.post(url, data=payload);
    return response.json()

if __name__ == '__main__':
    url = 'http://localhost:8080/test/01'
    data = '''
            { 
                "DOMAIN" : "bluemsp",
                "FROM_USER_ID" : "1001",
                "DATE_CREATED" : "2017-12-06-18-08-01",
                "DURATION" : "360",
                "TRANSCRIPT" : "testing transcripts generated by GSR API",
                "TO_USERS" : [
                            {"TO_USER_ID" : "1001"},
                            {"TO_USER_ID" : "1019"}
                            ]
            }
    '''

    print("request : ", data)
    rsl = post_cdr(url, data)
    print("post result : ", json.dumps(rsl, indent=4))

    payload = {'name':'Saravanan',
               "status" : "success",
                   'Designation':'Architect',
                   'Orgnization':'Cisco Systems',
                   'testing_str': "98",
                   "testing_int" : 99 }
    payld = json.dumps(payload, indent=4)
    print("payload : ", payld)
    rsl = post_cdr(url, payld)
    #print("post result, status : ", rsl.name);
    print("post result json : ", json.dumps(rsl, indent=4))
    if ('status' in rsl and rsl['status'] == "success") :
        print("post success : ", rsl["status"])
    else :
        print("post failed.");
        
    status = rsl.get("status", "failed")
    print("post status : ", status)

