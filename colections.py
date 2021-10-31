#colections exercise
#explain map,reduce and filter functions...

Map_function= print("the map function applies an N function to a sequence of elements and returns a new list with the modifications,receives as argument a function N and a list")

Reduce_function=print("The reduce function allows us to reduce a list to a single iterable element, it receives a function N and a list as parameters.")

Filter_function=print("the filter function receives as arguments a list and a function N and allows us to check if the elements of the list meet a certain condition.returns an iterable with the checked items.")


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




