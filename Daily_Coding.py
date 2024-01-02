# ops = ["5","-2","4","C","D","9","+","+"]
# ops = ["1"]
ops = ["5","2","C","D","+"]

# C :delete the latest point
# D: double the latest two scores
# +: add latest two scores
result = []
for i in range(len(ops)):
    if ops[i]=='C':
        result.pop(-1)
    elif ops[i]=='D':
        result.append(2*result[-1])
    elif ops[i]=='+':
        result.append(result[-1]+result[-2])
    else:
        result.append(int(ops[i]))
print(sum(result))

