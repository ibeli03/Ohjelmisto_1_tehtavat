import random
import math
def approximate_pi(num_points):
    inside = 0
    for _ in range(num_points):
        x = (random.randint(-1, 1))
        y = (random.randint(-1, 1))
        if (x^2 + y^2 <= 1):
            inside += 1
    pi_approx = 4* inside / num_points
    return pi_approx
num_points = int(input("Enter the number of random points to generate: "))
pi_approx = approximate_pi(num_points)
print(f"The approximate value of pi with the given random points is {pi_approx}")











