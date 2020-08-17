inputfilename = "input_index_7_1.txt"
outputfilename = "output_coordinates_7_1.txt"

inputfilehandle = open(inputfilename, 'r')
outputfilehandle = open(outputfilename, 'w')

#ignore the first line
inputfilehandle.readline()

L1 = 50
L2 = 57
outputfilehandle.write("x1\tx2\n")
while True:
    line = inputfilehandle.readline()
    if not line:
        break
    index = int(line.strip())
    x1 = index % L1
    x2 = index // L1
    outputfilehandle.write(str(x1))
    outputfilehandle.write("\t")
    outputfilehandle.write(str(x2))
    outputfilehandle.write("\n")
    
    
inputfilehandle.close()
outputfilehandle.close()
