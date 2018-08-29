HEX_COLOURS = {"moccasin": "#ffe4b5", "ivory2": "#eeeee0", "PaleGreen": "#98fb98", "rebeccapurple": "#663399",
             "thistle": "#d8bfd8", "gold1": "#ffd700", "chartreuse2": "#76ee00", "brown": "#a52a2a",
             "DeepPink3": "#cd1076", "gray64": "#a3a3a3"}

colour = input("Enter a colour name: ")
while colour != "":
    if colour in HEX_COLOURS:
        print("The hexadecimal code for ", colour, "is", HEX_COLOURS[colour])
    else:
        print("{} is an invalid colour".format(colour))
    colour = input("Enter a colour name: ")
