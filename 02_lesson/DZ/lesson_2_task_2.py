

def is_year_leap(year):
    if year % 4 == 0:
        return True 
    else: 
        return False
 
year = 1549
leap = is_year_leap(year)
print(f"год {year}:{leap}")