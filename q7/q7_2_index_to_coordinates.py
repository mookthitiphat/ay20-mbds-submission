inputfilename = "input_index_7_2.txt"
outputfilename = "output_coordinates_7_2.txt"

inputfilehandle = open(inputfilename, 'r')
outputfilehandle = open(outputfilename, 'w')

#ignore the first line
inputfilehandle.readline()

L = (4,8,5,9,6,7)
d = len(L)

for i in range(1,d+1):
    outputfilehandle.write("x")
    outputfilehandle.write(str(i))
    outputfilehandle.write("\t")
outputfilehandle.write("\n")

while True:
    line = inputfilehandle.readline()
    if not line:
        break
    index = int(line.strip())
    for i in range(d):
        product = 1
        for j in range(i):
            product *= L[j]
        x_i = (index // product) % L[i]
        if i != 0:
            outputfilehandle.write("\t")
        outputfilehandle.write(str(x_i))
    outputfilehandle.write("\n")
    
    
inputfilehandle.close()
outputfilehandle.close()
