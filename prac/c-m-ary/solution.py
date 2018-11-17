#!/usr/bin/python3

def gen_opts(m, n):
	cand = 1
	opts = []
	while True:
		opts.append(cand)
		cand *= m
		if cand > n:
			return opts

def sreduce(n, k, opts):
	if n == 0:
		return 1
	if n < 0:
		return 0
	if k == 0:
		return 0
	return ((n - opts[k - 1], k),
			(n, k - 1))
		
def fit_opts(n, k, opts):
	running = 0
	stack = []
	stack.append((n, k))
	while len(stack) > 0:
		elem = sreduce(*stack.pop(), opts)
		if type(elem) is tuple:
			stack.append(elem[0])
			stack.append(elem[1])
		else:
			running += elem
		#print(running, end="\r")
	return running
		
def fit_opts_recursive(n, opts):
	# If we've reached exactly zero,
	# that is one way to fit the options into N.
	if n == 0:
		return 1
	# If we're less than zero, that isn't
	# a way to fit the options into N.
	if n < 0:
		return 0
	# If there are no options, we can't do anything,
	# so don't count it
	if len(opts) == 0:
		return 0
	# Return largest fit, plus fitting for rest of list
	return \
	  fit_opts_recursive(n - opts[-1], opts) + \
	  fit_opts_recursive(n, opts[:-1])
		
def count_partitions(m, n):
	opts = gen_opts(m, n)
	print(fit_opts(n, len(opts), opts))

def get_input():
	set_count = int(input())
	sets = []
	for i in range(set_count):
		line = input()
		elems = line.split(' ')
		sets.append((int(elems[1]), int(elems[2])))
	return sets

sets = get_input()

for i, s in enumerate(sets):
	print("set {0} / m = {1} / n = {2}:".format(i, s[0], s[1]))
	count_partitions(*s)
