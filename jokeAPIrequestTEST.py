import requests
response = requests.get("https://official-joke-api.appspot.com/jokes/random")
joke = response.json()
print("="*50)
print(f"id: {joke['id']}\ntype : {joke['type']}\nsetup: {joke['setup']}\npunchline: {joke['punchline']}")
print("="*50)