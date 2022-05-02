#!/usr/bin/python3

import glob
import os
import re

pattern1 = re.compile(r"[a-z]", re.IGNORECASE)
read_files = glob.glob("*.lst")

alp='abcdefghijklmnopqrstuvwxyz'

for f in read_files:
    with open(f, "rt") as infile:
        lines=infile.readlines()
        line=lines[2].strip().split()[1]
        g=' '

        for i in range(10,0, -1):
            if re.search('___', lines[i]) != None:
                title_line=i

        title=lines[2]
        if title_line>3:
            for i in range(3,title_line):
                title = title.strip() +' ' + lines[i].strip()

        if pattern1.search(line) != None: # If a match is found
            result=re.search(r"[a-zA-Z]", line).start()
            g=line[result:]
        nums=line.split(".")
        lin=' '
        for h in nums:
            h=h.lower()
            h=h.strip(alp)
            if len(h)>1:
                h2=h
            elif len(h)==1:
                h2='0'+h
            else:
                h2=''
            lin += h2
        lin += g
        lin1=lin.replace(' ','') + ' ' + title.strip() + '.lst'
    os.rename(f,lin1)
