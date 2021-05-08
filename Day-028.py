"""
Day 28
python regex
https://www.hackerrank.com/domains/regex
"""

#https://www.hackerrank.com/challenges/matching-word-non-word/problem
Regex_Pattern = r"\w{3}\W\w{10}\W\w{3}"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

#https://www.hackerrank.com/challenges/matching-start-end/problem
Regex_Pattern = r"^\d\w{4}\.$"	# Do not delete 'r'.

#https://www.hackerrank.com/challenges/excluding-specific-characters/problem
Regex_Pattern = r'^[^\d][^aeiou][^dcDF][^\s][^AEIOU][^.,]$'

#https://www.hackerrank.com/challenges/matching-range-of-characters/problem
Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'
