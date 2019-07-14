import group_anagram
import pytest

solution = group_anagram.Solution()

def test_standard():
   i = ["eat", "tea", "tan", "ate", "nat", "bat"]
   expected_output = sorted([
           ["ate","eat","tea"],
           ["nat","tan"],
           ["bat"]
           ])
   output = sorted(solution.group_anagrams(i))
   
   for l in [output, expected_output]:
       for i in range(len(l)):
           l[i] = sorted(l[i])

   assert(sorted(expected_output) == sorted(output))

def test_empty_elements():
   i = ["",""]
   expected_output = [["",""]]
   output = sorted(solution.group_anagrams(i))

   assert(sorted(expected_output) == sorted(output))
