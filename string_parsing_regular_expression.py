import pandas as pd
import re

pattern = re.compile('^\$\d*\.\d{2}$')

result = pattern.match('$17.25')

print(bool(result))



prog = re.compile('\d{3}-\d{3}-\d{4}')

result = prog.match('123-456-7890')
print(bool(result))

result = prog.match('1123-456-7890')
print(bool(result))

matches= re.findall('\d+', 'the recipe calls for 10 strawberries and 1 banana')
print(matches)

# Write the first pattern
pattern1 = bool(re.match(pattern='\d{3}-\d{3}-\d{4}', string='123-456-7890'))
print(pattern1)

# Write the second pattern
pattern2 = bool(re.match(pattern='\$\d*\.\d{2}', string='$123.45'))
print(pattern2)

# Write the third pattern
pattern3 = bool(re.match(pattern='[A-Z]\w*', string='Australia'))
print(pattern3)