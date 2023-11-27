"""akjsd"""


f_input = input()
first_input = f_input.split(" ")
first_input = [int(x) for x in first_input]

s_input = input()
sec_input = s_input.split(" ")
sec_input = [int(x) for x in sec_input]

avarage = sum(sec_input)/first_input[0]

if first_input[1] == 100:
    for value in sec_input:
        if value != 100:
            print("impossible")
            exit()


while avarage < first_input[1]:
    sec_input.append(100)
    avarage = sum(sec_input) / len(sec_input)


print(len(sec_input) - first_input[0])
