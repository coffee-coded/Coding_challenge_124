if __name__ == "__main__":
    main_list = []
    print("Input Integers for array : ")
    while True:
        x = input()
        if x == "":
            break
        else:
            try:
                main_list.append(int(x))
            except:
                pass
    print("Array : ", main_list)
    k = 0
    flag = 0
    for i in range(len(main_list)):
        if sum(main_list[:k]) == sum(main_list[k + 1:]):
            if flag == 0:
                print("Yes")
            flag = flag + 1
            print("Element : ", main_list[k], " , at index : ", k)
        k = k + 1

    if flag == 0:
        print("No")
