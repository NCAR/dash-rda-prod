import glob
import sys
import xml.etree.ElementTree as ET
import os
from xml.etree.ElementTree import parse
import time
import xmltodict
import pprint
from gcmdsupport import getGCMDfromXML
import os
from os import path
from collections import Counter


path1 = '.'
if(path.exists("rda_gcmd.txt")):
    os.remove("rda_gcmd.txt")
fo = open("rda_gcmd.txt", "w+")

for filename in os.listdir(path1):
    if not filename.endswith('.xml'): continue
    fullname = os.path.join(path1, filename)
    keywords = getGCMDfromXML(fullname)
    for keyword in keywords:
        fo.writelines(keyword)
        fo.writelines("\n")

fo.close()

level1 = 0
level2 = 0
level3 = 0
level4 = 0
level5 = 0
level6 = 0

# with open('rda_gcmd.txt') as f:
#     seen = set()
#     for line in f:
#         line_lower = line.lower()
#         if line_lower in seen:
#             print(line)
#         else:
#             seen.add(line_lower)

if(path.exists("rda_gcmd_counts_levels.txt")):
    os.remove("rda_gcmd_counts_levels.txt")

sys.stdout = open("rda_gcmd_counts_levels.txt", "w")

with open('rda_gcmd.txt') as f:
     c=Counter(c.strip().lower() for c in f if c.strip()) #for case-insensitive search
     for line in c:
         if c[line]>1:
             level = line.count('>') + 1 
             if(level == 1):
                 level1 += 1
             elif(level == 2):
                 level2 += 1
             elif(level == 3):
                 level3 += 1
             elif(level == 4):
                 level4 += 1
             elif(level == 5):
                 level5 += 1
             elif(level == 6):
                 level6 += 1
             count = "Count: " + str(c[line])
             level = "Level " + str(level)
             fileline = ''.join((line, ' ', count, ' ', level, '\n'))
             print(fileline)

print("Level 1:", level1)
print("Level 2:", level2)
print("Level 3:", level3)
print("Level 4:", level4)
print("Level 5:", level5)
print("Level 6:", level6)

sys.stdout.close()