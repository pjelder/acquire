#!/usr/bin/env python

import sys
import random

pm = {}
p1s = {}
p2s = {}
pps = {}
hs = {}
gb = {}
sm = {}
bpps = {}

def init():
    for i in range (0,3):
        p1s[i] = 0
        p2s[i] = 0
        sm[i] = 30
        pps[i] = (i+1)*100
        bpps[i] = (i+1)*100
#        hs[i] = 0
        gb[i] = 0

    for i in range (1,3):
        pm[i] = 3000

    gb['e'] = 100
    gb['u'] = 0
    gb['o'] = 0


def print2():
    print 'pm:'
    for k,v in pm.iteritems():
        print k,v
    print 'p1s:'
    for k,v in p1s.iteritems():
        print k,v
    print 'p2s:'
    for k,v in p2s.iteritems():
        print k,v
    print 'pps:'
    for k,v in pps.iteritems():
        print k,v
#    print 'hs:'
#    for k,v in hs.iteritems():
#        print k,v
    print 'gb:'
    for k,v in gb.iteritems():
        print k,v
    print 'sm:'
    for k,v in sm.iteritems():
        print k,v

    p1w = pm[1]
    p2w = pm[2]
    for h in range (0,3):
        p1w += p1s[h]*pps[h]
        p2w += p2s[h]*pps[h]

    print 'p1w:',p1w
    print 'p2w:',p2w

def act():
    pa = []
    # u, h0, h1, h2, m0, m1, m2, n0, n1, n2, ??--np0, np1, np2?
    for t in range(0,6):
        sp = random.randint(1,(gb['e']+gb['u']+gb['o']))
        if sp <= (gb['e']-12):
            pa.append('u')
        sp = sp - (gb['e']-12)
        if sp<=0:
            continue

        for h in range(0,3):
            if sp <= gb[h]:
                pa.append('h'+str(h))
            sp = sp - gb[h]
            if sp<=0:
                break
        if sp<=0:
            continue

        for h in range(0,3):
            if ((gb[h] != 0) and (sp <= 2)):
                pa.append('m'+str(h))
                sp=0
                break
            sp = sp - 2
            if sp<=0:
                break
        if sp==0:
            continue

        for h in range(0,3):
            if ((gb[h] == 0) and (sp <= 2) and gb['u']>=2):
                pa.append('n'+str(h))
                sp=0
                break
            sp = sp - 2
            if sp<=0:
                break
        if sp==0:
            continue

    return pa

def sel(ch):
    if ch == 'u':
        gb['u']+=1
    elif ch == 'h0':
        gb[0]+=1
        gb['o']+=1
    elif ch == 'h1':
        gb[1]+=1
        gb['o']+=1
    elif ch == 'h2':
        gb[2]+=1
        gb['o']+=1
    elif ch == 'm0':
        mrg(0)
    elif ch == 'm1':
        mrg(1)
    elif ch == 'm2':
        mrg(2)
    elif ch == 'n0':
        gb['u']-=1
        gb[0]=2
        gb['o']+=2
    elif ch == 'n1':
        gb['u']-=1
        gb[1]=2
        gb['o']+=2
    elif ch == 'n2':
        gb['u']-=1
        gb[2]=2
        gb['o']+=2
    else:
        print 'error!!!'
    gb['e']-=1

def mrg(h):
    tgt = raw_input('mrg:')
    while tgt not in ['0','1','2']:
        print 'Not valid'
        tgt = raw_input('mrg:')
    tgt = int(tgt)
    if gb[h] >= gb[tgt]:
        gb[h]+= gb[tgt]+1
        gb[tgt]=0
    else:
        gb[tgt]+=gb[h]+1
        gb[h]=0
    gb['o']+=1

def mkt(ply):
    bys = 3
    while bys > 0:
        oht = []
        for h in range(0,3):
            if gb[h]!=0:
                oht.append(str(h))
        pht = raw_input('pht:')
        while (pht not in oht) and (pht!='q'):
            print 'Not valid'
            pht = raw_input('pht:')
        if pht=='q':
            break
        qny = raw_input('qny:')
        # TODO logic
        while ((int(qny) not in range(0,bys+1)) or (int(qny)>sm[int(pht)]) or (pm[ply]<qny*pps[int(pht)])):
            print 'Not valid'
            qny = raw_input('qny:')
        ord(ply,int(pht),int(qny))
        bys -= int(qny)
    
def ord(ply,ht,qny):
    sm[ht] -= qny
    pm[ply] -= (qny*pps[ht])
    if ply==1:
        p1s[ht]+=qny
    if ply==2:
        p2s[ht]+=qny

def spr():
    for k,v in pps.iteritems():
        if gb[k] < 10:
            pps[k]=bpps[k]*gb[k]
        else:
            pps[k]=10*bpps[k]*(gb[k]/10)


init()
while 1:
    print2()
    chc = act()
    print chc
    ch = raw_input('act:')
    while ch not in chc:
        print 'Not valid'
        ch = raw_input('act:')
    sel(ch)
    spr()
    mkt(1)




                                            #ak1 = random.randint(1,6)
                                            #if (ak1==1):
                                            #    continue
                                            #elif (ak1==6 or ak1 + cu1 - sh2 >= 6):
                                            #    hth2-=1
                                        #if hth2<=0:
                                        #    break
                                        #for ak in range(0,wp2):
                                        #    ak1 = random.randint(1,6)
                                        #    if (ak1==1):
                                        #        continue
                                        #    if (ak1==6 or ak1 + cu2 - sh1 >= 6):
                                        #        hth1-=1

