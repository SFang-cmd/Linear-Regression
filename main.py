
# input
coords = [(1, 36), (3,28), (5,16), (8,-1), (12,-6)]

# list declaration
x_list = []
y_list = []
x_sqr_list = []
xy_list = []

list_len = len(coords)

for num_elems in range(list_len):
	# adds the appropriate coordinate numbers to the lists
	x_list.append(coords[num_elems][0])
	y_list.append(coords[num_elems][1])
	x_sqr_list.append(x_list[num_elems]**2)
	xy_list.append(x_list[num_elems]*y_list[num_elems])

# summed lists
y_sum = sum(y_list)
x_sum = sum(x_list)
x_sqr_sum = sum(x_sqr_list)
xy_sum = sum(xy_list)

# a and b values for output
a = ((y_sum*x_sqr_sum) - (x_sum*xy_sum))/((list_len*x_sqr_sum) - (x_sum**2))

b = ((list_len*xy_sum) - (x_sum*y_sum))/((list_len*x_sqr_sum) - (x_sum**2))

# output: y = a + bx
print(str(a) + " + " + str(b) + "x")

def sum(num_list):
	sum = 0
	for iter in range(len(num_list)):
		sum = num_list[iter] + sum
	return sum