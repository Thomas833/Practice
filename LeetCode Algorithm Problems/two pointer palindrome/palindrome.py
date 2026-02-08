def main():
    o = open("outputFile.txt", "w")
    with open("inputFile.txt", "r") as f:
       while True:
            line = f.readline()
            if not line:
                break
            line = line.strip("\n")
            last = len(line) - 1
            for first in range(len(line)):
                msg = "first: " + str(first) + " | last: " + str(last)
                if first == last or (first + 1 == last and line[first] == line[last]):
                    o.write("Y | " + msg + " | " + line + "\n")
                    break
                else:
                    if line[first] == line[last]:
                        last -= 1
                        continue
                    else:
                        o.write("X | " + msg + " | " + line + "\n")
                        break
                
    o.close()
    f.close()
    print("done!")

            



main()