class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        len_A = len(A)
        if len_A != len(B):
            return False
        if A == B:
            return True
        for i in range(len_A):
            if A[i+1:len_A]+A[0:i+1] == B:
                return True
        return False