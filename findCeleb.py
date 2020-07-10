class Solution:
    def findCelebrity(self, n):
        
        def isCelebrity(celeb):
            
            for people in range (n):
            
                if people == celeb:
                    continue
                    if knows(celeb, people) or not knows(people, celeb):
                        return False
            return True
        candidateForCeleb = 0
        for person in range(1, n):
            if knows(candidateForCeleb, person):
                candidateForCeleb = person
        if isCelebrity(candidateForCeleb):
            return CandidateForCeleb
        return -1
 
