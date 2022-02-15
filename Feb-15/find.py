# find.py

def find(target, items):
    print("Canary")
    
def main():
    list_items = [ 2, 7, 132, 17, 11, 3, 10 ] 
    
    search_1 = 11
    # should return 4
    loc_1 = find(search_1)
    print(loc_1)

    serach_2 = -42
    # will not find any result, should return -1
    loc_2 = find(search_2)
    print(loc_2)
