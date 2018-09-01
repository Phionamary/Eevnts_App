# Load data files
ordinary_file = open("ordinary_list.txt", "r")
vip_file = open("vip_list.txt", "r")
# lists for storing names
ord_arr = []
vip_arr = []

# Store names in lists
for o in ordinary_file.readlines():
	ord_arr.append(o)

for v in vip_file:
	vip_arr.append(v)
	
def registration_checker(name):
	print(check_for_name(name))
		
	

# Method checks and returns names if in the lists	
def check_for_name(nm):
    
	# check and return matching names to arrays
	# if no matching names, arrays shall be empty
	# also convert all names to lower case for uniformity
	match_ord = [s for s in ord_arr if nm.lower() in s.lower()]
	match_vip = [s for s in vip_arr if nm.lower() in s.lower()]
	
	# Check length of array and return appropriate response
	if len(match_ord)>0:
		return match_ord[0]+" ORDINARY"
	elif len(match_vip)> 0:
		return match_vip[0]+" VIP"
	else:
		return "Not Registered"
	
name=input("Please enter your first name:")
		
# Call function to test
registration_checker(name)