import requests

print("==================== GET THE PUBLIC IP ADDRESS OF THE DEVICE ====================")
api_url = "https://ipapi.co/json"
response = requests.get(api_url)
api_response = response.json()

ip = api_response["ip"]
city = api_response["city"]
region = api_response["region"]
country = api_response["country_name"]
asn = api_response["asn"]
org = api_response["org"]

print("The public IP address of your system is: " + ip)
print("You are in estimated to be in " + city + " which is located in " + region + ", " + country)
print("Your internet service provider is " + org + ". The ASN of your provider is " + asn)


