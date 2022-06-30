import requests as re
import json

class API:
    
    def GET(self,url,body="NA"):
        lt={}
        try:
            if body != "NA":
                response_code=re.get(url,params=body)
                lt['response_code'] = response_code

                response_result = (json.dumps(response_code.json(),indent=4))

                lt['response_result'] = response_result
                lt['respose_headers'] = response_code.headers
                lt['response_content_type'] = response_code.headers['Content-Type']
                lt['response_cookies'] = response_code.cookies
            else:
                response_code=re.get(url)
                lt['response_code'] = response_code

                response_result = (json.dumps(response_code.json(),indent=4))

                lt['response_result'] = response_result
                lt['respose_headers'] = response_code.headers
                lt['response_content_type'] = response_code.headers['Content-Type']
                lt['response_cookies'] = response_code.cookies
        except Exception as e:
            return {'Error Message':e}
        return lt
    
    def POST(self,url,body="NA"):
        lt={}
        try:
            if body != "NA":
                response_code=re.get(url,params=body)
                lt['response_code'] = response_code

                response_result = (json.dumps(response_code.json(),indent=4))

                lt['response_result'] = response_result
                lt['respose_headers'] = response_code.headers
                lt['response_content_type'] = response_code.headers['Content-Type']
                lt['response_cookies'] = response_code.cookies
            else:
                response_code=re.get(url)
                lt['response_code'] = response_code

                response_result = (json.dumps(response_code.json(),indent=4))

                lt['response_result'] = response_result
                lt['respose_headers'] = response_code.headers
                lt['response_content_type'] = response_code.headers['Content-Type']
                lt['response_cookies'] = response_code.cookies
        except Exception as e:
            return {'Error Message':e}
        return lt
            


