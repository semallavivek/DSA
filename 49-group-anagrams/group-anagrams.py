class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dici = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key in dici:
                dici[key].append(i)
            else:
                dici[key] = [i]
        return(list( dici.values()))