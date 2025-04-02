from numpy import sort


a_list = [25, 16, 1, 8, 95, 22]
print(f"Original {a_list}")
b_list = sorted(a_list, reverse=False)
print(f"Method sorted {b_list}")
c_list = a_list
c_list.sort()
print(f"Method sort {c_list}")
d_list = ['Marina', 'Vladislav', 'Emma', 'Vadim',
          'Vasilii', 'Ekaterina', 'Arina', 'Mihail']
print(f"Method sorted with key {sorted(d_list, key=len)}")
