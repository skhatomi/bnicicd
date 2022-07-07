import requests

print("hello world")
print("testing cicd BNI")

response = requests.get("https://www.google.com")

#print (response.text)

waktu = datetime.now()

with open("tempResponse/" + waktu + ".txt", "w") as f:
    f.write(response.text)