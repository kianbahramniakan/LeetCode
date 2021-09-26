class Solution:
    def reverse(self, x: int) -> int:
        res = list(map(str, str(x)))
        if res[0] == '-':
            res.pop(0)
            for i in range(0, len(res)):
                res[i] = int(res[i])
            z = 1
        else:
            for i in range(0, len(res)):
                res[i] = int(res[i])
            z = 2
        
        q = len(res)
        
        y = []
        for i in range (len(res)):
            q = q - 1
            # print(res[q])
            y = y + [res[q]]
            if q == 0:
                if z == 2:
                    strings = [str(integer) for integer in y]
                    a_string = "".join(strings)
                    an_integer = int(a_string)
                    if  an_integer >= ((2**31)-1):
                        return 0
                    else:
                        return (an_integer)
        
                else:
                    strings = [str(integer) for integer in y]
                    a_string = "".join(strings)
                    an_integer = int(a_string)
                    an_integer = (an_integer)
                    if an_integer >= ((2**31)-1):
                        return 0
                    else:
                        return -(an_integer)
