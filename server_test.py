import requests


print("Adding an Item")
print(
    requests.post(
        "http://127.0.0.1:8000/",
        json={
            "name": "Scredriver", 
            "price":3.99, 
            "count":10, 
            "id":4, 
            # "category":"tools"
        },
    ).json()
)
print(requests.get("http://127.0.0.1:8000/").json())
print()


print("Updating an item:")
print(requests.put("http://127.0.0.1:8000/items/0?count=9001").json())
print(requests.get("http://127.0.0.1:8000/").json())
print()


print("Deleting an items")
print(requests.delete("http://127.0.0.1:8000/items/0").json())
print(requests.get("http://127.0.0.1:8000/").json())

