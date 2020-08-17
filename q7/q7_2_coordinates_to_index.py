inputfilename = "input_coordinates_7_2.txt"
outputfilename = "output_index_7_2.txt"

inputfilehandle = open(inputfilename, 'r')
outputfilehandle = open(outputfilename, 'w')

#ignore the first line
inputfilehandle.readline()

L = (4,8,5,9,6,7)
d = len(L)

outputfilehandle.write("index\n")
while True:
    line = inputfilehandle.readline()
    if not line:
        break
    X = line.strip().split()
    index = 0
    for i in range(d):
        X[i] = int(X[i])
        product = 1
        for j in range(i):
            product *= L[j]
        index += X[i]*product
    outputfilehandle.write(str(index))
    outputfilehandle.write("\n")
    
    
inputfilehandle.close()
outputfilehandle.close()
