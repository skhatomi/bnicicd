import requests

print("hello world")
print("testing cicd BNI")

response = requests.get("https://www.google.com")

print (response.text)