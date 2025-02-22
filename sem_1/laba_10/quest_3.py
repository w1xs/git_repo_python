from collections import deque

arr_of_tickets = []
arr_of_que = []
max_que_len = -1

with open("bank.txt") as file:
    for line in file:
        if line.strip() != '':
            one_que = deque()
            arr_of_tickets = line.strip().replace(',', '').split(' ')
            for ticket in arr_of_tickets:
                one_que.append(ticket)
            if len(one_que) > max_que_len:
                max_que_len = len(one_que)
            print(one_que)
            arr_of_que.append(one_que)

res_str = ""

for i in range(max_que_len):
    for que in arr_of_que:
        if len(que) > 0:
            if i + 1 != max_que_len:
                res_str += que.popleft()
                res_str += ', '
            else:
                res_str += que.popleft()

print(res_str)
