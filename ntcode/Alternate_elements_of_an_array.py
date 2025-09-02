class AltnerativeArray:
    def __init__(self, arr: list):
        self.arr = arr

    def _secondArray_(arr: list):
        result = []
        for i in range(0, len(arr), 2):
            result.append(arr[i])
        return result

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    instantiate = AltnerativeArray
    print(str(instantiate._secondArray_(arr)))