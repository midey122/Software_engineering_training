database = [
    {
        'name': 'ade', 'pass': '123'
    },
    {
        'name': 'seun', 'pass': '12345'
    }, {
        'name': 'bayo', 'pass': '123gh5%'
    }
]

name = "ade"


for item in database:
    if item["name"] == "bayo":
        print(item)