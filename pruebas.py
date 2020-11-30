import json
base='{"usuarios": ["mica@mail.co", "jerry@gma.com","alber@soup.co"],"contra": ["abc123","caballitos","yoloswag"]}'

d= json.loads(base)
print(d["usuarios"][1])

for key,value in d:
    print(key)
    

            

    
