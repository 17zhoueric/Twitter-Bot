import math

# read all lines into list 'lines'
with open("tbotcb.txt", "r") as file:
    lines = file.readlines()
# pretty print
with open("tbotcb_edited.txt", "w") as file:
    # for every line in list 'lines' ...
    for line in lines:
        # if line is not blank ...
        if line != "\n":
            # if line exceeds twitter char limit ...
            if len(line) > 280:
                fractals = math.ceil(len(line) / 280)
                # split this line up into fractals
                for j in range(fractals):
                    if len(line) > 280:
                        index = 279
                        # if the fractal line is in the middle of a word ...
                        while line[index] != " ":
                            index -= 1
                        file.write(line[:index] + "\n")
                        line = line[index:]
                    else:
                        file.write(line[:len(line)])
            else:
                file.write(line)

