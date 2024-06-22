def new_pass(n):
    clear_list = []
    for i in range(1, 21):
        for j in range(i, 21):
            if (i + j) % n == 0:
                clear_list.append(f"{i}{j}")

    result = ",".join(clear_list)
    return result
#for n in range(3, 21):
n = int(input("Введите число от 3 до 21:"))
print(f"{n} - {new_pass(n)}")











