import copy

def add_one(v):
    v += 1

def update_dict(my_dict):
    my_dict["a"] = 123
    add_one(my_dict["b"])
    d2 = copy.copy(my_dict)
    d2["c"]["d"] = 234

if __name__ == "__main__":
    d = {"a": 1, "b": 2, "c": {"d": 5}}
    d1 = d
    update_dict(d1)
    print("d['a'] ==", d["a"])  # 123
    print("d['b'] ==", d["b"])  # 2
    print("d['c'] ==", d["c"])  # {'d': 234}
    print(d)
    print(d1)
