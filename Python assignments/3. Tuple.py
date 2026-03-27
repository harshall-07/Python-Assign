tpl = ()
print(type(tpl))

tpl = (20 ,)                                     #for single element
print(tpl)

tpl1 = (10 , 12, 43)                               #tuple 1
print(tpl1)
print(tpl1[1])

tpl2 = (55 , 66, 77)                               #tuple 2

tpl3 = tpl1 + tpl2                              #concatineting tuple
print(tpl3)

tpl4 = (tpl1 , tpl2)                            #nested tuple
print(tpl4)
print(tpl4[0][1])

tuple = (3 , 4, 5)*3
print(tuple)

