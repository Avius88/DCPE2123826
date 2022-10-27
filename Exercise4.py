
# Press the green button in the gutter to run the script.


if __name__ == '__main__':

    def calc_average_temperature(listavg):
        total = 0

        for x in listavg:
            total = total+int(x)

        average = total/len(listavg)
        print("The average is",average)

    def calc_min_max_temperature(listminmax):
        max = listminmax[0]
        min = listminmax[0]

        for x in listminmax:
            if x > max:
                max = x
            else:
                if x < min:
                    min = x

        print("The maximum value is",max,"and the minimum value is",min,".")



    print('Exercise 4 \n')

    userlist = []
    count = 0
    userinput = ""

    print("Input 'start' to execute script!")
    while userinput != "start":
        userinput = input("Input list entry   :\n")
        if userinput != "start":
            userlist.append(userinput)
            #print(userlist)


    print("-- Script Start --")
    print(userlist," was input")

    calc_average_temperature(userlist)
    calc_min_max_temperature(userlist)
