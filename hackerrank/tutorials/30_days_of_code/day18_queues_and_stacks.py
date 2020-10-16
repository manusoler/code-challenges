import sys

class Solution:
    
    def __init__(self):
        self.queue = []
        self.stack = []
    
    def pushCharacter(self, ch):
        self.stack.append(ch)

    def enqueueCharacter(self, ch):
        self.queue.insert(0, ch)

    def popCharacter(self):
        ch = self.stack[-1]
        del self.stack[-1]
        return ch

    def dequeueCharacter(self):
        ch = self.queue[-1]
        del self.queue[-1] 
        return ch

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

# push/enqueue all the characters of string s to stack
for i in s:
    obj.pushCharacter(i)
    obj.enqueueCharacter(i)
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    