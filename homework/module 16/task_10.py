def palindrome_check(pal_num):
    reverse_list = list(pal_num)
    reverse_list.reverse()
    if pal_num == reverse_list:
        return True
    else:
        return False

num_list =  [1, 2, 1, 3, 2, 1, 1, 1, 1]
new_nums = []
answer = []

for x in range(len(num_list)):
    for check in range(x, len(num_list)):
        new_nums.append(num_list[check])
    if palindrome_check(new_nums):
        for i_answer in range(0, x):
            answer.append(num_list[i_answer])
        answer.reverse()
        break
    new_nums = []

print(num_list, answer)
num_list.append(list(answer))
print(num_list)
