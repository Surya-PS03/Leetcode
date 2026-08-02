class Solution:
    def partitionString(self, s: str) -> List[str]:

        N = len(s)
        occ = set()
        segment = ""
        res = []
        for char in s:
            segment += char
            if segment not in occ:
                occ.add(segment)
                res.append(segment)
                segment = ""

        return res

