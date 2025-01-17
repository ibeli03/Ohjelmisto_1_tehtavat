import random
combination1 = "".join(str(random.randint(0, 9)) for _ in range(3))
combination2= "".join(str(random.randint(0, 9)) for _ in range(3))
print(f"The first random 3-digit combination: {combination1} ")
print(f"The second random 3-digit combination: {combination2}")

combination3="".join(str(random.randint(1, 6)) for _ in range(4))
combination4="". join(str(random.randint(1, 6)) for _ in range(4))
print(f"The first random 4-digit combination: {combination3}")
print(f"The second random 4-digit combination: {combination4}")
