#google ==> True
#g00gle ==> True
#g()Og|3 ==> True


import itertools

string = input()

    
O = ['o','0','()','[]','<>']
L = ['l','|','i']
E = ['e','3']
G = ['g']
cases = []
case= ''

for (i,j) in list(itertools.combinations(O, 2)):
    for l in L:
        for e in E:
            cases.append('g'+i+j+'g'+l+e)
            cases.append('g'+j+i+'g'+l+e)
            cases.append('g'+i+i+'g'+l+e)
            cases.append('g'+j+j+'g'+l+e)

if string.lower() in cases:
    print(True)
else:
    print(False)
