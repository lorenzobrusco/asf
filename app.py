from asf.core import RestApi
from asf.api import HttpMethod
from asf.response import BaseResponse

app = RestApi()

def handler(event: any, context: any) -> BaseResponse:
    return app.execute(event, context)

@app.route('api1', method=HttpMethod.GET, has_any_roles=['CrifStudioAws_Admin'])
def api1_func(event: any, context: any) -> BaseResponse:
    print("api1")
    print(event)
    print(context)
    
@app.route('api2', method=HttpMethod.GET, has_any_roles=['CrifStudioAws_Admin'])
def api2(event: any, context: any) -> BaseResponse:
    print("api2")
    print(event)
    print(context)
    
@app.route('api2',  method=HttpMethod.POST)
def api3(event: any, context: any) -> BaseResponse:
    print("api3")
    print(event)
    print(context)
    
print(handler({
        "body": "{\"name\":\"test_pycsc_3\",\"encryption\":\"true\",\"value\":\"blallo2\",\"region\":\"eu-central-1\",\"accountId\":\"914007954673\"}",
        "resource": "/{proxy+}",
        "path": "api1",
        "httpMethod": "GET",
        "queryStringParameters": {},
        "pathParameters": {},
        "requestContext": {
            "authorizer": {
            "roles": "CrifStudioAws_Admin,,internal"
            }
        }
    }, 
    'blallo')
)