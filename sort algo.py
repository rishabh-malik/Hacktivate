import numpy as np 

inside = np.array([6, 13, 6])

outside = np.array([9, 8, 17])

max_num = np.array([20, 20, 20])


total_after = inside + outside

def show_colour(arr, max_num):
	for i in range(len(arr)):
		if (arr[i] >= max_num[i]+2):
			print("Red", end=" ")
		elif (arr[i] >= (max_num[i]-3)):
			print("Yellow", end=" ")
		else:
			print("Green", end=" ")
	print("\n")


def balance(inside, outside, max_num, total_after):
	
	prev_extra = 0
	extra = 0

	for i in range(len(total_after)):

		prev_extra = extra
		extra = total_after[i] - max_num[i]

		#print(extra, prev_extra)

		if(extra > prev_extra):
			outside[i] = outside[i] - extra
			outside[i-1] = outside[i-1] + extra
			#print(outside)

		else:
			outside[i] = outside[i] - extra
			outside[i+1] = outside[i+1] + extra
			#print(outside)

	print(outside)	

show_colour(total_after, max_num)
balance(inside, outside, max_num, total_after)
show_colour(total_after, max_num)
