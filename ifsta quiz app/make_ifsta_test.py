# -*- coding: utf-8 -*-
"""
Created on Wed May 15 08:12:38 2019

@author: Marshall
"""

import re

html_tag_template = open("html_tag_template.txt","r")

questions = open("ifsta_questions_good.txt", "r")

file = open("ifsta_testing.html","a")


for line in html_tag_template:
    m = re.search("</body>", line)
    n = re.search("</html>", line)
    if m or n:
        continue
    else:
        file.write(line)
        print("yes")

file.write("<script>\n")

file.write("let ifstaQuestions=\n")

for qline in questions:
    file.write(qline)

file.write("\n\n</script>\n")

file.write("</body>\n")
file.write("</html>\n")

questions.close()
html_tag_template.close()
file.close()