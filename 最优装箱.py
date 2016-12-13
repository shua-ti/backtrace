#-*-coding=utf-8-*-
#!/usr/bin/env python
"最优装箱问题"



def loading(weight,c1):
    bestw = []
    pattern = []
    p = [0] * len(weight)
    def load(c1, k=0, cw=0):
        if cw > c1: return
        if k == len(weight):
            if cw <= c1:
                bestw.append(cw)
                p_copy = list(p)
                pattern.append(p_copy)
            return

        cw += weight[k]
        p[k] = 1
        load(c1, k + 1, cw)
        cw -= weight[k]
        p[k] = 0
        load(c1, k + 1, cw)
    load(c1)
    if sum(weight)-max(bestw) <=c2:
        print "可以顺利装箱："
    return pattern[bestw.index(max(bestw))]

if __name__=="__main__":
    weight=[90,80,40,30,20,12,10]
    c1=152
    c2=130
    pattern=loading(weight,c1)
    print pattern



