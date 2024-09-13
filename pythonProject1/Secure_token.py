import secrets
#Genereate a secure random token

token = secrets.token_hex(16)
print(f"Secure Token: {token}")

#Genereate a secure random url
url_safe_token = secrets.token_urlsafe(16)
print(f"Secure url: {url_safe_token} ")

#Genereate a secure random int
random_int = secrets.randbelow(200)+1
print(f"Secure Random Number: {random_int}")

#Genereate a secure random list
itens= ['banan','wisna']
random_inems = secrets.choice(itens)
print(f"Losowy obiekt {random_inems}")

print("sdfsdf")