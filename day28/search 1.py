import re
str = 'man sun mop run'
prog = re.compile(r'm\w\w')
result = prog.search(str)
if result: 
    print(result.group())
