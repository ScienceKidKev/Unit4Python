my_file=open('kevaughn.txt', 'a')

#print(my_file.readlines())

my_file.write(' im writing from pyhton\n')

my_file.close()

my_file=open('kevaughn.txt')

for line in my_file.readlines():
    print(line, end='')


