def gen_num(start,end):
    while start <= end:
        yield start
        start += 1
num_list = []
for i in gen_num(6, 13):
    num_list.append(i)

print(num_list)