def largest_sum(numbers: list[int]) -> tuple[int, int]:
    status = bool(numbers)
    while status:
        if len(numbers) > 1:
            primeiro = max(numbers)
            iMax = numbers.index(primeiro)
            numbers.pop(iMax)
    
            segundo = max(numbers)
    
            return segundo, primeiro
        else:
            return None
        
    return None
    
if __name__=="__main__":
    largest_sum([0, 0, 0, 0])
