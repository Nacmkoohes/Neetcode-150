class Solution:

#encode : ["neet","code","love","you"] -> 4#neet4#code4#love3#you
    def encode(self, strs: list[str]) -> str:
        res=""
        for word in strs:
            res+=str(len(word))+"#"+word
        return res


    def decode(self, s: str) -> list[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            res.append(s[j+1:j+1+length])
            i=j+1+length
        return res




