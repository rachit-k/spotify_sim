def code2val(code):
    if(code=="0"):
        return [0,0.2]
    if(code=="1"):
        return [0.2,0.4]
    if(code=="2"):
        return [0.4, 0.6]
    if(code=="3"):
        return [0.6, 0.8]
    if(code=="4"):
        return [0.8,1.1]

def pcode2val(code):
    if(code=="0"):
        return [0,20]
    if(code=="1"):
        return [20,40]
    if(code=="2"):
        return [40, 60]
    if(code=="3"):
        return [60, 80]
    if(code=="4"):
        return [80,101]

def lcode2val(code):
    if(code=="0"):
        return [4,-5]
    if(code=="1"):
        return [-5,-17]
    if(code=="2"):
        return [-17, -29]
    if(code=="3"):
        return [-29, -42]
    if(code=="4"):
        return [-42,-55]

def tcode2val(code):
    if(code=="0"):
        return [0,30]
    if(code=="1"):
        return [30,60]
    if(code=="2"):
        return [60, 90]
    if(code=="3"):
        return [90, 150]
    if(code=="4"):
        return [150,240]