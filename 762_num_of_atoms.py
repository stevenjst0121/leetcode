from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        """Draft 1
        Using stack, logic is a bit messy. Solution is very similar and make use of Collections
        """
        stack = []
        curr_name = None
        i = 0
        while i < len(formula):
            if formula[i] == "(":
                if curr_name:
                    stack.append([curr_name, 1])
                    curr_name = None
                stack.append(formula[i])
                i += 1
            elif formula[i] == ")":
                if curr_name:
                    stack.append([curr_name, 1])
                    curr_name = None
                stack.append(formula[i])
                i += 1
            elif formula[i].isnumeric():
                curr_num = int(formula[i])
                j = i + 1
                while j < len(formula) and formula[j].isnumeric():
                    curr_num = curr_num * 10 + int(formula[j])
                    j += 1

                if curr_name:
                    stack.append([curr_name, curr_num])
                    curr_name = None
                else:
                    stack.pop()  # this must be ")"
                    updated_formula = []
                    while stack and stack[-1] != "(":
                        updated_formula.append(stack.pop())
                        updated_formula[-1][1] = updated_formula[-1][1] * curr_num
                    stack.pop()  # this must be "("
                    stack.extend(updated_formula)
                i = j
            elif formula[i].isupper():
                if curr_name:
                    stack.append([curr_name, 1])
                    curr_name = None
                curr_name = formula[i]
                j = i + 1
                while j < len(formula) and formula[j].islower():
                    curr_name += formula[j]
                    j += 1
                i = j
        if curr_name:
            stack.append([curr_name, 1])

        # print result
        atoms_count = defaultdict(int)
        for atom in stack:
            if atom == "(" or atom == ")":
                continue
            atoms_count[atom[0]] += atom[1]

        result = ""
        for atom in sorted(atoms_count.keys()):
            result += atom
            count = atoms_count[atom]
            if count > 1:
                result += str(count)
        return result
