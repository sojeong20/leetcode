class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        letter_map = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }
        
        list_of_letters_list = [letter_map.get(digit) for digit in digits]
        combinations = itertools.product(*list_of_letters_list)
        
        return ["".join(combination) for combination in combinations]