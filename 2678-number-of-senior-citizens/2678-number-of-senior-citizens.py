class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # [phoneNumber(10)+gender(1)+age(2)+seat(2)] total = 15
        return sum(s[11:13] > '60' for s in details)
        