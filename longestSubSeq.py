#s1 = 'ABABSLMDHS',s2 = 'ABSDJKDJKABSDQWSAJDSJHS' ==> 'ABABSDHS'

def longestSubSeq(str1='ABABSLMDHS',str2='ABSDJKDJKABSDQWSAJDSJHS'):
    result = []
    temp = ''
    tempstr2 = str2
    while len(str1)>1:
        str2 = tempstr2
        for idx1,s1 in enumerate(str1):
            for idx2,s2 in enumerate(str2):
                if s2==s1:
                    temp += s1
                    str2 = str2[idx2+1:]
                    break
        if len(temp)>0 and temp not in result:            
            result.append(temp)
        temp = ''
        str1 = str1[1:]
    #print(result)
    if len(result) == 0:
        return 'No Common Sequence found..'
    return max(result,key=len)
