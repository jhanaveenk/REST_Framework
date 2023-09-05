import requests

# endpoint = "https://httpbin.org/#/Status_codes/get_status__codes_"
endpoint="https://httpbin.org/anything"

get_response = requests.get(endpoint)
print(get_response.json())