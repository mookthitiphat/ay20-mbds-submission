inputfilename = "input_coordinates_7_1.txt"
outputfilename = "output_index_7_1.txt"

inputfilehandle = open(inputfilename, 'r')
outputfilehandle = open(outputfilename, 'w')

#ignore the first line
inputfilehandle.readline()

L1 = 50
L2 = 57
outputfilehandle.write("index\n")
while True:
    line = inputfilehandle.readline()
    if not line:
        break
    x1,x2 = line.strip().split()
    x1 = int(x1)
    x2 = int(x2)
    index = x2*L1 + x1
    outputfilehandle.write(str(index))
    outputfilehandle.write("\n")
    
    
inputfilehandle.close()
outputfilehandle.close()
