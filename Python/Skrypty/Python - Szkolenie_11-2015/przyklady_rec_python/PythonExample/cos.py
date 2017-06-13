"""
x = 27
while x > 0:
    print x
    if x > 30:
        break
    else:
        x -= 1
"""

"""
# statement-based while loop
while <cond>:
    <pre-suite>
    if <break_condition>:
        break
    else:
        <suite>
# FP-style recursive while loopp
def while_block():
    <pre-suite>
    if <break_condition>:
        return 1
    else:
        <suite>
        return 0
while_FP = lambda: (<cond> and while_block()) or while_FP() while_FP()
"""
"""
x = 27

def wBlock():
    global x
    x -= 1
    print x
    return False if x > 0 else True

whileFP = lambda: ( wBlock() or whileFP())

whileFP()

#print wBlock()
        
"""
x = 30
def wBlock():
    global x
    print x
#    if x > 30:
#        return False
#    else:
#        x -= 1
#        return True
    x -= 1
    return False if x > 31 else True

wFP = lambda: ( x > 0 and wBlock()) and wFP()

wFP()
