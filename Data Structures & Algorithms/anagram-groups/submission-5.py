class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)

        for i in strs:
            key = [0]*36
            for j in i:
                key[ord(j)- ord("a")+1] += 1
            hmap[tuple(key)].append(i)

        return list(hmap.values())
