import unittest
import itertools
from main import *

class UnitTests(unittest.TestCase) :
    def test_combinations(self) :
        for i in range(2,8) : 
            for j in range(i+1) : 
                student_combinations = gencombinations(i,[i-j,j])
                base = i*[0] 
                for k in range(j) : base[k] = 1 
                for seq in set(itertools.permutations(base)) : 
                    found=False
                    for sseq in student_combinations : 
                        isseq=True 
                        for k in range(len(seq)) : 
                            if seq[k]!=sseq[k] : isseq=False
                        if isseq : 
                           found=True
                           break
                    self.assertTrue( found, "Your code for generating all the combinations is not working" )
