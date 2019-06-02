myfile = open("example.txt", "w")
myfile.write("Something")
myfile.close()


with open("example.txt", "w") as myfile:
    myfile.write("Something")


temperatures = [10, -20, -289, 100]
"""" def c_to_f(c):
    if c < -273.15:
        return "That temperatur doesn't make sense"
    else:
        f = c * 9/5 + 32
        return f
for t in temperatures:
    with open("temperatures.txt", "w") as mytemp:
        mytemp.write(str(c_to_f)) """

def writer(temperatures):
    with open("temperatures.txt", "w") as mytemp:
        for c in temperatures:
            if c > -273.15:
                f = c * 9/5 + 32
                mytemp.write(str(f) + "\n")

writer(temperatures) # output of the function
