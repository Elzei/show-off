__author__ = 'jedrzej.polaczek'

base = "{{{{{},{},{},{},{},{},{},{}}},{{{}}}}}, //{}"

argss = [[bool(byte>>bit & 1) for bit in range(8)] for byte in [value for value in range(0x0100)]]

c = 1
for i in argss:
    v = i+[len([x for x in i if x == True]), c]
    print(base.format(*v))
    c += 1

