# playin with json
# Author : Atacan Buyuktas

import json
data = {
    'name': 'Atacan',
    'age': 32,
    "student":True
}
jsonString = json.dumps(data)
print (data)
print (jsonString)