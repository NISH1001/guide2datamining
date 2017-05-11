#!/usr/bin/env python3

def pearson_coefficient(x_vec, y_vec):
    """
        This function finds the Pearson Correlation Coefficient between two data set
    """
    n = len(x_vec)
    if len(y_vec) != n:
        raise ValueError("Both the vectors should have same length")

    # r is coefficient
    sum_xy, sum_x, sum_y, sum_xsq, sum_ysq = 0, 0, 0, 0, 0
    for i in range(n):
        sum_xy += x_vec[i] * y_vec[i]
        sum_x += x_vec[i]
        sum_y += y_vec[i]
        sum_xsq += x_vec[i] ** 2
        sum_ysq += y_vec[i] ** 2
    numerator = (sum_xy - sum_x * sum_y / n)
    denominator =   ((sum_xsq - sum_x*sum_x / n ) ** 0.5) * ((sum_ysq - sum_y*sum_y / n ) ** 0.5) 
    if denominator == 0:
        return 0
    return numerator/denominator

def magnitude(x_vec):
    """
        Find the magnitude of the given vector
    """
    s = 0
    for x in x_vec:
        s += x**2
    return s**0.5

def dot_product(x_vec, y_vec):
    """
        Find the dot product between two vectors
    """
    n = len(x_vec)
    if len(y_vec) != n:
        raise ValueError("Both the vectors should have same length")
    dot = 0
    for i in range(n):
        dot += x_vec[i] * y_vec[i]
    return dot

def cosine_similarity(x_vec, y_vec):
    """
        Find the cosine similarity between two vectors
    """
    return dot_product(x_vec, y_vec) / ( magnitude(x_vec) * magnitude(y_vec) )

def main():
    x = [4.75, 4.5, 5, 4.25, 4]
    y = [4, 3, 5, 2, 1]
    r = pearson_coefficient(x, y)
    cosine = cosine_similarity(x, y)
    print(r)
    print(cosine)

if __name__ == "__main__":
    main()

