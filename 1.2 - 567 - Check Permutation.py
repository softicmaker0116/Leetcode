def checkInclusion(s1, s2):
    # sol.2 - t=O(s1s2);s=O(s1)
    # The reason why the sol.2 is much more faster:
    # For each loop in sol.1, you sum all values in dict & cmp the result to zero
    # For each loop in sol.2, you only cmp two dict
    dic1 = {}
    dic2 = {}
    len_s1 = len(s1)
    for c in s1: 
        if c in dic1: 
            dic1[c]+=1
        else: 
            dic1[c]=1
    for c in s2[:len_s1]:
        if c in dic2: 
            dic2[c] += 1
        else: 
            dic2[c] = 1

    for i in range(len(s2)-len_s1):
        if dic2 == dic1: return True # check results of every run except the last run 
        if dic2[s2[i]] > 1: 
            dic2[s2[i]] -= 1
        else: 
            del dic2[s2[i]]
        if s2[i+len_s1] not in dic2: 
            dic2[s2[i+len_s1]] = 1
        else: 
            dic2[s2[i+len_s1]] += 1

    if dic2 == dic1: # check the last result
        return True
    return False

    """ sol1. check sum - t=O(s1s2);s=O(s1)
    if len(s1)>len(s2):
        return False;
    dic={x:0 for x in s1};
    for i in s1:
        dic[i]+=1;
    # print("init:", dic);
    for start in range(0,len(s2)): # O(s2)
        end = start+len(s1);
        sum1 = 0;
        if end>len(s2):
            continue;
        if start==0:
            for k in s2[start:end]:
                if k in dic:
                    dic[k]-=1;
        else:
            if s2[start-1] in s1:
                dic[s2[start-1]]+=1;
            if s2[end-1] in dic:
                dic[s2[end-1]]-=1;
        for value in dic.values(): # O(s1)
            sum1+=abs(value);
        # print(start, ":", end, s2[start:end], dic, sum1);
        if sum1==0:
            return True;
    else:
        return False;
    """

result = checkInclusion("ab", "cccabccc")
print(result)