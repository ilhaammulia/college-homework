from functools import reduce

def filterData(n):
        return True if n % 3 == 0 else False

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    genap = [n for n in data if n % 2 == 0]
    
    mapping = list(map(lambda x: x * 2, genap))
    filtering = list(filter(filterData, mapping))
    reducing = reduce(lambda x, y: x + y, filtering)
    print("Raw Data:", data)
    print("Data Mapping:", mapping)
    print("Data Filtering:", filtering)
    print("Data Reduce:", reducing)
    
