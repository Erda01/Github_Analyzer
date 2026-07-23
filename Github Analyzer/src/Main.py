import requests

username = input("Enter the Github Username: ")
while not username:
    username = input("Please, Enter the Github Username: ")

url = f"https://api.github.com/users/{username}"

response = requests.get(url)


if response.status_code == 200:

    data = response.json()

    print("Name:", data["name"])
    print("Followers:", data["followers"])
    print("Following:", data["following"])
    print("Public Repositories:", data["public_repos"])
    print("Location:", data["location"])
    print("Bio:", data["bio"])
else:
    print(f"Github Username: {username} was not found.")


