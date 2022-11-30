import re
str='man sun mop run'
result=re.search(r'm\w\w',str)
if result:
    print(result.group())
