import json

# import test1
# import test2 as t2

obj = """
{
"name":"Wes",
"palce_lived":["a","b"],
"pet":null
}
"""

result = json.loads(obj)
print(result)
print(result["name"])
print(result["palce_lived"])
print(result["pet"])
# print (t2.add(1, 2))
