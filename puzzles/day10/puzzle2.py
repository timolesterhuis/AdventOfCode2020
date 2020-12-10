from collections import Counter
import math

with open("puzzles/day10/puzzle_input.txt") as f:
    data = f.read().splitlines()


adapters = sorted([int(d) for d in data] + [0])
adapters.append(max(adapters)+3)
differences = [b - a for a, b in zip(adapters[:-1], adapters[1:]) ]
diff = lambda d: [d[i+1]-d[i] for i in range(len(d)-1)]

count = Counter(differences)
#count[3] += 1

a = "".join([str(d) for d in differences])
b = a.split("3")
c = [2**(len(i)-1) for i in b if i]

def tri(n):
	result = [0,0,1]
	for i in range(3,n+3):
		result.append(sum(result[-3:]))

	return result[1:]

c = []
streak = 1
for i in range (0, len(adapters)):
		if adapters[i]-adapters[i-1] == 1:
			streak +=1

		else:
			if streak > 1:
				c.append(tri(streak-1)[-1])
				streak = 1
                
solution = math.prod(c)


print(f"Solution is {solution}")
