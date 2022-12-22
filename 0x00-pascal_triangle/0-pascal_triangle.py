#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        if (i + 1 >= 2):
            row.append(1)
            for j in range(1, i):
                previous = triangle[i - 1]
                row.append(previous[j - 1] + previous[j])
        row.append(1)
        triangle.append(row)

    return triangle
