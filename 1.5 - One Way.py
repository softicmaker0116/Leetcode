def OneWay(t1,t2):
    len_t1 = len(t1)
    len_t2 = len(t2)
    if len_t1 < len_t2:
        return OneWayChk(t1,t2,len_t1,len_t2)
    return OneWayChk(t2,t1,len_t2,len_t1)

def OneWayChk(t1,t2,len_t1,len_t2):
    pt1, pt2 = 0, 0
    first_diff = 0
    while pt1 < len_t1 and pt2 < len_t2:
        # print(first_diff, t1[pt1], t2[pt2])
        if t1[pt1] != t2[pt2]:
            if first_diff == 1:
                return False
            if len_t1 == len_t2:
                pt1+=1
            pt2+=1
            first_diff = 1
            continue
        pt1, pt2 = pt1+1, pt2+1
    return True

t1,t2 = "accd","abce"
result = OneWay(t1,t2)
print(result)