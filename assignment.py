import datetime
from sympy import symbols, Eq, solve,Integer

def fun(D):

    Do = {
        "mon":0,
        "tue":0,
        "wed":0,
        "thurs":0,
        "fri":0,
        "sat":0,
        "sun":0
            }

    check = [False,False,False,False,False,False,False]
    x, y, z, x1, y2 = symbols('w,x,y,x1,y2')

    for i in D:
        a = datetime.datetime.strptime(i, '%Y-%m-%d').weekday() 
        check[a] = True

        if a == 0:
            Do["mon"] +=  D[i]

        elif a == 1:
            Do["tue"] +=  D[i]

        elif a == 2:
            Do["wed"] +=  D[i]

        elif a == 3:
            Do["thurs"] +=  D[i]

        elif a == 4:
            Do["fri"] +=  D[i]

        elif a == 5:
            Do["sat"] +=  D[i]

        elif a == 6:
             Do["sun"] +=  D[i]


    count = 0

    for j in range (1, len(check)-1):
        
        if check[j] == False:

            if j == 1:
                if Do["wed"] == 0:
                    count += 1
                else:
                    Do["tue"] +=  Integer((Do["mon"]+Do["wed"])/2)

            elif j == 2:
                if Do["thurs"] == 0:
                    count += 1
                else:
                    if count == 0:
                        Do["wed"] +=  Integer((Do["tue"]+Do["thurs"])/2)

                    elif count == 1:
                        eq1 = Eq(Do["mon"]+y-2*x) 
                        eq2 = Eq(x+Do["thurs"]-2*y) 
                        sol_dict = solve((eq1, eq2), (x, y))
                        Do["tue"] = Integer(sol_dict[x])
                        Do["wed"] = Integer(sol_dict[y])
                        count = 0


            elif j == 3:
                if Do["fri"] == 0:
                    count += 1
                else:
                    if count == 0:
                        Do["thurs"] +=  Integer((Do["wed"]+Do["fri"])/2)

                    elif count == 1:
                        eq1 = Eq(Do["tue"]+y-2*x) 
                        eq2 = Eq(x+Do["fri"]-2*y) 
                        sol_dict = solve((eq1, eq2), (x, y))
                        Do["wed"] = Integer(sol_dict[x])
                        Do["thurs"] = Integer(sol_dict[y])
                        count = 0

                    elif count == 2:
                        eq1 = Eq(Do["mon"]+y-2*x) 
                        eq2 = Eq(x+z-2*y) 
                        eq3 = Eq(y+Do["fri"]-2*z)
                        sol_dict = solve((eq1, eq2, eq3), (x, y, z))
                        Do["tue"] = Integer(sol_dict[x])
                        Do["wed"] = Integer(sol_dict[y])
                        Do["thurs"] = Integer(sol_dict[z])
                        count = 0
                

            elif j == 4:

                if Do["sat"] == 0:
                    count += 1
                else:
                    if count == 0:
                        Do["fri"] +=  Integer((Do["thurs"]+Do["sat"])/2)

                    elif count == 1:
                        eq1 = Eq(Do["wed"]+y-2*x) 
                        eq2 = Eq(x+Do["sat"]-2*y) 
                        sol_dict = solve((eq1, eq2), (x, y))
                        Do["thurs"] = Integer(sol_dict[x])
                        Do["fri"] = Integer(sol_dict[y])
                        count = 0

                    elif count == 2:
                        eq1 = Eq(Do["tue"]+y-2*x) 
                        eq2 = Eq(x+z-2*y) 
                        eq3 = Eq(y+Do["sat"]-2*z)
                        sol_dict = solve((eq1, eq2, eq3), (x, y, z))
                        Do["wed"] = Integer(sol_dict[x])
                        Do["thurs"] = Integer(sol_dict[y])
                        Do["fri"] = Integer(sol_dict[z])
                        count = 0

                    elif count == 3:
                        eq1 = Eq(Do["mon"]+y-2*x) 
                        eq2 = Eq(x+z-2*y) 
                        eq3 = Eq(y+x1-2*z)
                        eq4 = Eq(z+Do["sat"]-2*x1)
                        sol_dict = solve((eq1, eq2, eq3, eq4), (x, y, z, x1))
                        Do["tue"] = Integer(sol_dict[x])
                        Do["wed"] = Integer(sol_dict[y])
                        Do["thurs"] = Integer(sol_dict[z])
                        Do["fri"] = Integer(sol_dict[x1])
                        count = 0
                
            elif j == 5:
                if count == 0:
                    Do["sat"] +=  Integer((Do["fri"]+Do["sun"])/2)

                elif count == 1:
                    eq1 = Eq(Do["thurs"]+y-2*x) 
                    eq2 = Eq(x+Do["sun"]-2*y) 
                    sol_dict = solve((eq1, eq2), (x, y))
                    Do["fri"] = Integer(sol_dict[x])
                    Do["sat"] = Integer(sol_dict[y])
                    count = 0

                elif count == 2:
                    eq1 = Eq(Do["wed"]+y-2*x) 
                    eq2 = Eq(x+z-2*y) 
                    eq3 = Eq(y+Do["sun"]-2*z)
                    sol_dict = solve((eq1, eq2, eq3), (x, y, z))
                    Do["thurs"] = Integer(sol_dict[x])
                    Do["fri"] = Integer(sol_dict[y])
                    Do["sat"] = Integer(sol_dict[z])
                    count = 0

                elif count == 3:
                    eq1 = Eq(Do["tue"]+y-2*x) 
                    eq2 = Eq(x+z-2*y) 
                    eq3 = Eq(y+x1-2*z)
                    eq4 = Eq(z+Do["sun"]-2*x1)
                    sol_dict = solve((eq1, eq2, eq3, eq4), (x, y, z, x1))
                    Do["wed"] = Integer(sol_dict[x])
                    Do["thurs"] = Integer(sol_dict[y])
                    Do["fri"] = Integer(sol_dict[z])
                    Do["sat"] = Integer(sol_dict[x1])
                    count = 0

                elif count == 4:
                    eq1 = Eq(Do["mon"]+y-2*x) 
                    eq2 = Eq(x+z-2*y) 
                    eq3 = Eq(y+x1-2*z)
                    eq4 = Eq(z+y2-2*x1)
                    eq5 = Eq(x1+Do["sun"]-2*y2)
                    sol_dict = solve((eq1, eq2, eq3, eq4, eq5), (x, y, z, x1, y2))
                    Do["tue"] = Integer(sol_dict[x])
                    Do["wed"] = Integer(sol_dict[y])
                    Do["thurs"] = Integer(sol_dict[z])
                    Do["fri"] = Integer(sol_dict[x1])
                    Do["sat"] = Integer(sol_dict[y2])
                    count = 0


    return Do



# D = {
#     "2020-1-1":4,
#     "2020-1-2":4,
#     "2020-1-3":6,
#     "2020-1-4":8,
#     "2020-1-5":2,
#     "2020-1-6":-6,
#     "2020-1-7":2,
#     "2020-1-8":-2,
# }

D = {
    "2021-2-1":2,
    "2021-2-5":3,
    "2021-2-7":14,
}

print(fun(D))