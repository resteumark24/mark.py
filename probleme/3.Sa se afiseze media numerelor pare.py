#l = []
#num = int(input("How many numbers: "))
#for i in range(num):
#  numbers = int(input("Enter number: "))
#  l.append(numbers)
#print(sum(l)//3)






#l = []
#num = int(input("How many numbers: "))
#for i in range(num):
#  numbers = int(input("Enter number: "))
#  l.append(numbers)
#for i in range(num):
#  numarPrim = i / 2
#  if numarPrim == 0:
#    print(sum(numarPrim) // len(num))

#[METODA FINALA]
#import statistics

#list = []
#num = int(input("How many numbers: "))
#for i in range(num):
#  numbers = int(input("Enter number: "))
#  list.append(numbers)
#x = statistics.mean(list)
#print(x)





import statistics

list = []
num = int(input("How many numbers: "))
for i in range(num):
  numbers = int(input("Enter number: "))
  list.append(numbers)
  x = statistics.mean(numbers)
for i in range(num):
  numarPrim = i / 2
  if numarPrim == 0:
    print(sum(numarPrim) // len(num))
