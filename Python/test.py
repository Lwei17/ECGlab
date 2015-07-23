print 3.0/11
x = np.array([1,2])
y = np.array([3,4])

print sum(x*y)
print np.sum(x*y)**2

a = {}

a.setdefault("a",0)
print a
a["a"] = 1
a.setdefault("a",0)
a["a"]+=1
print a

print a.has_key('a')