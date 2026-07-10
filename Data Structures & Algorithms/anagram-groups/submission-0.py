def checkAnagram(str1, str2):
    dict1, dict2 = dict(), dict()
    for s in str1:
        if s in dict1: dict1[s] += 1
        else: dict1[s] = 0
    for s in str2:
        if s in dict2: dict2[s] += 1
        else: dict2[s] = 0
    if len(dict1) != len(dict2):
        return False
    
    for key, value in dict1.items():
        if key not in dict2:
            return False
        else:
            if value != dict2[key]:
                return False
    return True

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramList = []
        groupSet = set()
        i = 0
        while i < len(strs):
            if i not in groupSet:
                j = i + 1
                subList = [strs[i]]
                while j < len(strs):
                    if not j in groupSet and checkAnagram(strs[i], strs[j]):
                        subList.append(strs[j])
                        groupSet.add(i)
                        groupSet.add(j)
                    j += 1
                anagramList.append(subList)
            i += 1

        return anagramList



        