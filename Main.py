# 
def perulangan(n):
    if n < 10:
        print(f"Perulangan ke-{n}")
        
        # increment
        perulangan(n+1)
    
    return 0

perulangan(5)