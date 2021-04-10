import re
a=re.compile(r"\d{2} \d{10}")#matches number of size 2+10
a.search("this is number: +91 1234567890")

print(re.compile(r"dd|aa").search("ddaa"))

re.compile(r"bat(wo)?man").search("batman")

re.compile(r"bat(wo)*man").search("batwowowowowowoman")

re.compile(r"(\d{3}) (\d{10})").search("111 1234567890").groups()

re.compile(r"(app){3,5}").search("appappappappapp")
re.compile(r"(app){3}|(app){4}|(app){5}").search("appappappappappappapp")

re.compile(r"\d+").search("123feji3i3")

#https://www.hackerrank.com/challenges/matching-specific-string/problem
Regex_Pattern = r'hackerrank'	# Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, "The hackerrank team is on a mission to flatten the world by restructuring the DNA of every company on the planet. We rank programmers based on their coding skills, helping companies source great programmers and reduce the time to hire. As a result, we are revolutionizing the way companies discover and evaluate talented engineers. The hackerrank platform is the destination for the best engineers to hone their skills and companies to find top engineers")

print("Number of matches :", len(match))

re.search(r"A.B","ANB")

re.findall('^.{2}',"asting\ngg")

re.search("\s{2}\S{2}","  sd")

re.search("\w{2}\W{2}","1W#$")
