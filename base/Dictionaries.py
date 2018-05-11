dic = {
    "name":"Jenson",
    "age":24,
    "color":[255,123,0],
    33:77
}
print(dic)
print(dic["name"])
print(dic["age"])
print(dic["color"])
print(dic[33])
dic["name"] = "yucheng"
print(dic)
dic["new_item"] = "this is a new one"
print(dic)

print("name" in dic)
print("Jenson" in dic)

pairs = {1: "apple",
  "orange": [2, 3, 4],
  True: False,
  None: "True",
}

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))