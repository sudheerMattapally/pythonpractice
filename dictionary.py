# mydict={

#     "id":1,
#     "name":"John",
#     "age":30
# }
# print(mydict["name"])
# print(mydict["age"]) 
# x=mydict.values()
# print(x)
# y=mydict.keys()
# print(y)
# x=mydict.get('id')
# print(x)
# mydict["age"]=35
# print(mydict)
# mydict["age"]=35
# mydict.update({"age":40})
# print(mydict)
# mydict.pop("age")
# mydict.popitem()
# print(mydict)
# del mydict["age"]
# print(mydict)
# mydict.clear()
# print(mydict)
# for x in mydict:
#     print(x)
# for x in mydict.values():
#     print(x)    
# for key,values in mydict.items():
#     print(key,values)

# mydict1=mydict.copy()
# # print(mydict1)
# mydict1=dict(mydict)
# print(mydict1)

parent={

    "child1":{
        "name":"John",
        "age":30,
        "city":"New York"
    },
    "child2":{
        "name":"Jane",
        "age":25,
        "city":"Los Angeles"
    }
}
print(parent)
