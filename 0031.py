a_list = []
for i in range(100):
    a_list.append(i)

for i in range(len(a_list)):
    a_list[i] = a_list[i]*a_list[i]
print(a_list)
