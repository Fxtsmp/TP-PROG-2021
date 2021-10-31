#colections exercise

#algorithm for number pi with n number of numbers...










#point Nº2..

def List(list,num):
    if num==0:
        return list
    else:
        list.append(num)
        num=num-1
        return   List(list,num)

num=int(input("enter a number: "))
lista=[]
new_list=List(lista,num)

#map function..

Map=list(map(lambda num: 4-((-1)**num)/(2*num)+1,new_list))

print(Map)
#function filter...

Filtrado=list(filter(lambda numero: numero <= 3.14,Map))

print(Filtrado)




