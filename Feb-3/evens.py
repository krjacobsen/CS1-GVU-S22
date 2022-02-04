# evens.py

def evens(items):
    """ Return list of even values in items. """
    result = []
    for item in data:
        if item % 2 == 0:
            # result += list(item)
            result += [item]
    
    return result
    
def main():
    data = [93, 32, 28, 2, 56, 99, 17, 14, 3]
    even_data = evens(data)
    
    print(even_data)

main()