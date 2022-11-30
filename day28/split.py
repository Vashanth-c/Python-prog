import re
str = 'This; is the:"Core" '
result = re.split(r'\w+', str)
print(result)
