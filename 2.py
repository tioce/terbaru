# uncompyle6 version 3.3.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Apr  6 2019, 01:42:57) 
# [GCC 8.3.0]
# Embedded file name: dg
import os, sys, time, random
from sys import exit as keluar
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from sys import stdout
from os import system
m = '\x1b[1;91m'
h = '\x1b[1;92m'
k = '\x1b[1;93m'
b = '\x1b[1;94m'
u = '\x1b[1;95m'
c = '\x1b[1;96m'
p = '\x1b[0m'
i = '\x1b[1;90m'
v = '\x1b[1;38;5;198m'
j = '\x1b[1;38;5;208m'
w = (m, v, j, p, k, b, u, c)
W = pilih(w)

def load():
    l = 'H '
    a = 'A '
    g = 'C '
    i = 'K '
    n = '  '
    P = 'F '
    r = 'A '
    h = 'C '
    w = 'E '
    u = 'B '
    o = 'O '
    s = 'O '
    e = 'K '
    S = '  '
    for z in range(20):
        waktu(0.1)
        stdout.write('\r              \x1b[39;1m[\x1b[32;1m+\x1b[39;1m]\x1b[1;36m ' + n[(z % len(n))] + n[(z % len(n))] + l[(z % len(l))] + a[(z % len(a))] + g[(z % len(g))] + i[(z % len(i))] + n[(z % len(n))] + P[(z % len(P))] + r[(z % len(r))] + h[(z % len(h))] + w[(z % len(w))] + u[(z % len(u))] + o[(z % len(o))] + s[(z % len(s))] + e[(z % len(e))] + S[(z % len(S))] + n[(z % len(n))] +' \x1b[39;1m[\x1b[32;1m+\x1b[39;1m]')
        stdout.flush()



load()
