def arithmetic_arranger(problems, showresult = False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    problemsAsList = []
    for problem in problems:
        pList = problem.split()
        if (pList[1] == '+'):
            try:
                result = (int(pList[0]) + int(pList[2]))
            except ValueError as verr:
                return "Error: Numbers must only contain digits."
        elif (pList[1] == '-'):
            try:
                result = (int(pList[0]) - int(pList[2]))
            except ValueError as verr:
                return "Error: Numbers must only contain digits."
        else:
            return "Error: Operator must be '+' or '-'."
        pList.append(str(result))
        problemsAsList.append(pList)
    nums = ''
    dens = ''
    ops = ''
    res = ''
    sep =''
    espace = ''
    i= 0
    for p in problemsAsList:
        if(i>0):
            espace = '    '
        maxL = len(p[0])
        if len(p[2]) > len(p[0]):
            maxL = len(p[2])
        
        if len(p[0]) < 5:
            nums+= espace
            nums += (p[0].rjust(maxL+2,' '))
        else:
            return 'Error: Numbers cannot be more than four digits.'
        if len(p[2]) < 5:
            dens += espace
            dens += (p[1])
            dens += (p[2].rjust(maxL+1,' '))
        else:
            return 'Error: Numbers cannot be more than four digits.'
        #ops += (p[1])
        #print(maxL)
        sep += espace
        sep += ''.rjust(maxL+2,'-')
        res += espace
        res += (p[3].rjust(maxL+2,' '))
        i = i+1
    arranged_problems = f"{nums}\n" +f"{dens}\n" + f"{sep}\n"+ f"{res}" if showresult else f'{nums}\n'+f'{dens}\n'+f'{sep}'
    return arranged_problems