class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictA = {}
        dictB = {}

        for c in magazine:
            dictB[c] = dictB.get(c, 0) + 1

        for c in ransomNote:
            dictA[c] = dictA.get(c, 0) + 1
            if c not in dictB or dictA[c] > dictB[c]:
                return False
        return True

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in ransomNote:
            if c not in magazine:
                return False
            magazine = magazine.replace(c, '', 1)
        return True
