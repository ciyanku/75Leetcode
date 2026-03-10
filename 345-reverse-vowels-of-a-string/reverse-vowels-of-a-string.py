class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=[]
        for ch in s:
            if ch  in "aeiouAEIOU":
                vowels.append(ch)

        result=[]

        for ch in s:
            if ch in "aeiouAEIOU":
                result.append(vowels.pop())
            else:
                result.append(ch)
        return "".join(result)