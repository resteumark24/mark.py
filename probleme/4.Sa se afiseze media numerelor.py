import statistics

list = []
num = int(input("How many numbers: "))
for i in range(num):
  numbers = int(input("Enter number: "))
  list.append(numbers)
result = statistics.mean(i for i in list if i % 2 ==0)
print(result)
