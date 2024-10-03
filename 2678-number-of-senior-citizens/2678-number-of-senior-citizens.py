class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # [phoneNumber(10)+gender(1)+age(2)+seat(2)] total = 15
        total = 0
        
        for person in details:
            age = person[11] + person[12]
            if int(age) > 60:
                total += 1
                
        return total
        