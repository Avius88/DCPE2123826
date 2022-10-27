

if __name__ == '__main__':

    def calc_median_temperature(listmedian):
        
        sortedlist = sorted(listmedian)
        listlen = len(listmedian)
        index = (listlen -1) //2

        if (listlen&2):
            print("Median is",sortedlist[index])
        else:
            print("Median is",(sortedlist[index] + sortedlist[index+1])/2)
                  

    print('Exercise 6 \n')

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


    calc_median_temperature(userlist)
