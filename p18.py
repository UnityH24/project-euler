cache = {}

def find_max_path(triangle, start):
    row, col = start
    val = triangle[row][col]
    if row == len(triangle) - 1:
        return val
    if cache.get(start) is not None:
        return cache[start]
    left, right = (row + 1, col), (row + 1, col + 1)
    left_max, right_max = find_max_path(triangle, left), find_max_path(triangle, right)
    result = val + max(left_max, right_max)
    cache[start] = result
    return result

def main():
    triangle = [
            [3],
           [7, 4],
          [2, 4, 6],
         [8, 5, 9, 3]
    ]
    start = (0, 0)
    print(find_max_path(triangle, start))

if __name__ == "__main__":
    main()

