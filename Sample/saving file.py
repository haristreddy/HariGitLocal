import statistics as s

example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]

x = s.mean(example_list)
print(x)

y = s.median(example_list)
print(y)

z = s.mode(example_list)
print(z)

a = s.stdev(example_list)
print(a)

b = s.variance(example_list)
print(b)

g = s.harmonic_mean(example_list)
print (g)
