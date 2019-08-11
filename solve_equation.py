import re
class Solution:
    def compute(self, equation: str) -> str:
        left = equation[:equation.find("=")]
        right = equation[equation.find("=")+1:]
        
        left_terms = self.get_terms(left)
        right_terms = self.get_terms(right)

        c_left, num_left = self.combine_like_terms(left_terms)
        c_right, num_right = self.combine_like_terms(right_terms)

        left_expression = c_left - c_right
        right_expression = num_right - num_left

        if left_expression == 0 and right_expression != 0:
            return "No solution"
        elif left_expression == 0 and right_expression == 0:
            return "Infinite solutions"
        else:
            simplified_right = int(right_expression/left_expression)
            solution = "x=" + str(simplified_right)
            return solution

    def get_terms(self, expression):
        sub_expression = expression.replace("-", "+-")
        terms = sub_expression.split("+")
        non_null_terms = [t for t in terms if t != ""]
        return non_null_terms

    def combine_like_terms(self, terms):
        coefficients = []
        nums = []
        for t in terms:
            if "x" in t:
                term = t[:t.find("x")]
                if term == "-":
                    coefficients.append(-1)
                elif term:
                    coefficients.append(int(t[:t.find("x")]))
                else:
                    coefficients.append(1)
            else:
                nums.append(int(t))
        
        return sum(coefficients), sum(nums)

