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
                return "Error: Numbers must only contain digits"
        elif (pList[1] == '-'):
            try:
                result = (int(pList[0]) - int(pList[2]))
            except ValueError as verr:
                return "Error: Numbers must only contain digits"
        else:
            return "Error: Operator must be '+' or '-'"
        pList.append(str(result))
        problemsAsList.append(pList)
    nums = ''
    dens = ''
    ops = ''
    res = ''
    sep =''
    for p in problemsAsList:
        if len(p[0]) < 5:
            nums += (p[0].rjust(6,' '))+('    ')
        else:
            return 'Error: Numbers cannot be more than four digits'
        dens += (p[1])
        if len(p[2]) < 5:
            dens += (p[2].rjust(5,' '))+('    ')
        else:
            return 'Error: Numbers cannot be more than four digits'
        #ops += (p[1])
        sep += '______    '
        res += (p[3].rjust(6,' '))+('    ')
    arranged_problems = f"{nums}\n{dens}\n{sep}\n{res}" if showresult else f"{nums}\n{dens}\n{sep}"
    return arranged_problems