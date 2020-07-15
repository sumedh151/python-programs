#list
l1=["this","is","a","list"]
l2=[12,"mixed list",3.45,["nested list",23,4.54343]]
l3="this is a string".split("is")
l4=list((1,2,3,4,5,6,7,8,9,10))
l5=[i for i in range(10,20)]
print("l1 : {0}\nType of l1 : {1}\nLength : {2}\n".format(l1,type(l1),len(l1)))
print("l2 : {0}\nType of l2 : {1}\nLength : {2}\n".format(l2,type(l2),len(l2)))
print("l3 : {0}\nType of l3 : {1}\nLength : {2}\n".format(l3,type(l3),len(l3)))
print("l4 : {0}\nType of l4 : {1}\nLength : {2}\n".format(l4,type(l4),len(l4)))
print("l5 : {0}\nType of l5 : {1}\nLength : {2}\n".format(l5,type(l5),len(l5)))
print("l1[3] : ",l1[3])
l1[2]="a replaced "
print("New l1 : ",l1)
print("l2[3] : ",l2[3])
print("l2[3][1] : ",l2[3][1])
print("l2[3][0][2:] : ",l2[3][0][2:])
l1.append("this is a added string")
print("l1.append(this is a added string) : ",l1)
l2.extend("this is a added string".split())
print("l2.extend(this is a added string) : ",l2)
l2[3].append("adding to nested list")
print("l2[3].append(adding to nested list) : ",l2)
l2[3].extend("extending a nested list".split())
print("l2[3].extend(extending a nested list.split()) : ",l2)
print("l2.index(3.45) : ",l2.index(3.45))
print("l2[3].index(23) : ",l2[3].index(23))
l2[3].reverse()
print("l2[3].reverse() : ",l2)
l4.insert(4,[x*4 for x in range(10,20)])
print("l4.insert(4,[x*4 for x in range(10,20)]) : ",l4)
l6=l5.copy()
print("l6=l5.copy() : ",l6)
l5.reverse()
print("l5.reverse() : ",l5)
l5.sort()
print("l5.sort() : ",l5)
l5.sort(reverse=True)
print("l5.sort(reverse) : ",l5)
print("l5.pop(4) : ",l5.pop(4))
print("l5 : ",l5)
l5.remove(18)
print("l5.remove(18) : ",l5)
l5.clear()
print("l5.clear() : ",l5)
print("\r")
 
#tuple
t1=("this","is","a","tuple")
t2=tuple(i*3 for i in range(0,20,2))
print("t1 : ",t1)
print("t2 : ",t2)
print("Type of t1 : ",type(t1))
print("Type of t2 : ",type(t2))
print("len(t1) : ",len(t1))
print("len(t2) : ",len(t2))
print("t1[1] : ",t1[1])
print("t1[2:] : ",t1[2:])
print("t1[:2] : ",t1[:2])
print("any(t1) : ",any(t1))
print("all(t1) : ",all(t1))
print("t2[:2:-1] : ",t2[:2:-1])
print("t2[2::-1] : ",t2[2::-1])
print("t2[slice(4)] : ",t2[slice(4)])
print("t2[slice(1,5)] : ",t2[slice(1,5)])
print("t2[slice(1,8,3)] : ",t2[slice(1,8,3)])
print("t2.index(36) : ",t2.index(36))
print("min(t2) : ",min(t2))
print("max(t2) : ",max(t2))
print("sum(t2) : ",sum(t2))
#adding inserting removing cant be done because tuples are immutable but entire tuple can be deleted
del t1
#print(t1) will raise an error
print("\r")
 
#dictionaries
d1={
    "key1":"This is a dictionary",
    "key2":234.453,
    "key3":{
        "a":"Nested1",
        "b":12.31,
        "c":34,
        "d":[i for i in range(10)],
        "e":{
            1:3,
            2:(3,4,2,1,6),
            3:"test".split(),
            4:[c for c in "This is a test string"]
        }
    }
}
 
print("d1 : ",d1)
print("Type of d1 : ",type(d1))
print("For d1 : ")
print("Key\tValue")
for k,v in d1.items():
    print("{0}\t{1}".format(k,v))
print("\r")
print("For d1[key3] : ")
print("Key\tValue")
for k,v in d1["key3"].items():
    print("{0}\t{1}".format(k,v))
print("\r")
print("For d1[key3][e] : ")
print("Key\tValue")
for k,v in d1["key3"]["e"].items():
    print("{0}\t{1}".format(k,v))
print("\r")
print("d1.get(key2) : ",d1.get("key2"))
d2=dict.fromkeys([i for i in range(0,10)],(4,5))
print("d2 : ",d2)
print("d2.pop(5) : ",d2.pop(5))
print("d2.popitem() : ",d2.popitem())
d1.update(d2)
print("d1.update(d2) : ")
print("Key\tValue")
for k,v in d1.items():
    print("{0}\t{1}".format(k,v))
print("\r")
print("d1.keys() : ",d1.keys())
print("d1.values() : ",d1.values())
d2.clear()
print("d2.clear : ",d2)

