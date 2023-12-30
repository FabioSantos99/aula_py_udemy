import copy

d1 = {
      'c1': 1,
      'c2': 2,
      'c3': [0, 1, 2],
}


d2 =  copy.deepcopy(d1)


d2['c3'][1] = 56934

print(d1)
print(d2)