# writing data into text file
path = r'D:\Qspider\python selenium marathahalli\filehandling\demo'
# print(path)
with open(path, "w") as file:
    file.write("Hai this is file handling\n")
    file.write("Hello every one\n")
    file.write("this is web scraping\n")

# Reading data from file
with open(path, "r") as file:
    # read()
    data = file.read()
    print(data)
    print(len(data))
    # readline()
    data1 = file.readline()
    data2 = file.readline()
    print(data1, data2)
    print(type(data1))
    # readlines()
    data3 = file.readlines()
    print(data3)
    print(type(data3))
