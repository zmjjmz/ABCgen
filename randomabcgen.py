#!/usr/bin/python

import sys
import random

out = sys.argv[1]

songlength = 60
meter = "4/4"
notevalue = "1/4"
key = "C"
title = out
out = out + '.abc'


class note:
    def __init__(self, arg):
        super(note, self).__init__()
        self.arg = arg
        self.note = note
        self.length = length

class bar:
    """Simple class to make sure note lengths add up correctly"""
    def __init__(self, arg):
        super(note, self).__init__()
        self.notes = []
        self.capacity = capacity
        self.current = 0
    def add(self, note):
        if note.length + current <= capacity:
            length = note.length
            self.notes.append(note)
            if note.length[0] = "/":
                length = 1/int(length.pop())
                
            current += length
            return True
        else:
            return False

outFile = open(out, 'w')

header = []
header.append("X:1")
header.append("T:" + title)
header.append("M:" + meter)
header.append("L:" + notevalue)
header.append("K:" + key)

headers = "\n".join(header) + "\n"



stopAt = 32
depths = []
i = 2
while not(i == stopAt):
    depths.append(i)
    i = i*2
song = []
Allnotes = []
basenotes = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        ]

for i in basenotes:
    for j in range(int(meter[0])):
        if j == 0 or j == 1: continue
        Allnotes.append(note(i,j))    
        Allnotes.append(note(i + ",",j))
        Allnotes.append(note(i.lower(),j))
        Allnotes.append(note(i.lower() + "'",j))
    for j in depths:
        Allnotes.append(note(i,"/" + j))    
        Allnotes.append(note(i + ",","/" + j))
        Allnotes.append(note(i.lower(),"/" + j))
        Allnotes.append(note(i.lower() + "'","/" + j))


basenotes = []
#note lengths -- up to a whole note, down to 32 / note value
for j in range(int(meter[0])):
    if j == 0 or j == 1: continue
    for i in Allnotes:
        basenotes.append(i + str(j))
# this number acts as a max depth

for i in Allnotes:
    for j in depths:
        basenotes.append(i + "/" + str(j))

Allnotes = basenotes + Allnotes
    

for i in range(songlength):
    pick = random.randint(0,len(Allnotes)-1)
    if i % int(meter[0]) == 0:
        song.append("|")
    if random.uniform(0,1) > 0.5:
        song.append(" ")
    song.append(Allnotes[pick])
song.append(" |]")

notation = "".join(song)

complete = headers + notation

outFile.write(complete)
outFile.close()
