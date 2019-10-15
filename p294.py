import numpy as np
import re
import csv
import argparse

from h0 import *
from h1 import *
from h2 import *
from h3 import *
from h4 import *
from h5 import *
from h6 import *
from h7 import *
from events import *
from interEvents import *

def getHeader(line):
    new_line = re.findall("^[H]+[0][0]+[\d]+[0-8]+", line)
    if new_line:
        if line[0:5] == "H0000":
            getH0000(line)
        if line[0:5] == "H0001":
            getH0001(line)
        if line[0:5] == "H0002":
            getH0002(line)
        if line[1:5] == "H0003":
            getH0003(line)
        if line[0:5] == "H0004":
            getH0004(line)
        if line[0:5] == "H0005":
            getH0005(line)
        if line[0:5] == "H0006":
            getH0006(line)
        if line[0:5] == "H0007":
            getH0007(line)

def getComments(line):
    new_line = re.findall("^[C]+[\d][\d]+[\d]+[\d]+", line)
    if new_line:
        getC000x(line)

def getEvents(line,cells):
    new_line = re.findall("^[E]+[0-9]{4}", line)
    if new_line:
        if line[0:5] == "E1000":
            E1 = getE1000(line)
            cells[0] = E1.lineName+";"+E1.lineName[0:1]+";"+E1.shotNumber+";"+E1.date+";"+E1.time+";"
            return ""
        if line[0:3] == "E34":
            E34 = getE34x0(line)
            header = cells[0]
            str = header + E34.gunArrayNumber+";"+E34.gunNumber+";"+E34.p0+";"+E34.p1+";"+E34.p2+";"+E34.p3+";"+E34.p4+";"+E34.p5+";"+E34.p6+";"+E34.p7
            return str        

def getTimeEvents(line):
    new_line = re.findall("^[T]+[0-9]{4}", line)
    if new_line:
        print(new_line)

def openFile(filename, mode="r"):
    try:
        f = open(filename,mode)
        lines = []
        cells = ["header"]
        lines.append("Line;Base/Monitor;Shot Number;Date;Time;Gun Array Number;Gun Number;p0;p1;p2;p3;p4;p5;p6;p7")
        resultFile = filename + ".csv"
        for i,line in enumerate(f):
            #getHeader(line)
            #getComments(line)
            str = getEvents(line,cells)
            #rint(header)
            if not str:
                continue
            else:
                lines.append(str)
            #getTimeEvents(line)
            #data = line.split(" ")
            #print(len(data))
            #for j,dt in enumerate(data):
            #    print(data[j])
            #exit()
        fwrite = open(resultFile, 'w')
        fwrite.write("\n".join(lines))
        fwrite.close()

    except:
        f.close()
        raise

    return f

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, required=True)
    parser.add_argument('--mode', type=str, required=True)
    args = parser.parse_args()
    print(args)
    openFile(args.file,args.mode)
