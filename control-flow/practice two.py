#fruits_list = ['apples' , 'bananas', 'grapes', 'watermelon']
#print(fruits_list[1])
#bdict = {'title': 'Rangers Apprentice', 'author': 'John Flanagan', 'genre': 'Adventure'}
#def funcd(b,x):
    #if b in x:
        #print(x[b])
    #else:
        #print("Not Found")
#funcd('genre',bdict)
import random
ran_numbers = [random.randint(1,10) for _ in range(10)]
unique_numbers = set(ran_numbers)
print(ran_numbers)
print(unique_numbers)