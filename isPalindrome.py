class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = list(map(str, str(x)))
        if res[0] == '-':
            res.pop(0)
            for i in range(0, len(res)):
                res[i] = int(res[i])
            p = 1
        else:
            for i in range(0, len(res)):
                res[i] = int(res[i])
            p = 2
        y = 0
        qq = len(res) / 2
        q = len(res) - 1
        l = 0
        z = 0
        for i in range (len(res)):
            if p == 1:
                return False
                exit()
            if res[y] == res[q]:
                l = l + 1 
            elif res[y] != res[q]:
                l = 0
                z = z + 1
            if z > 0:
                return False
            elif l > qq:
                return True
            y = y + 1
            q = q - 1