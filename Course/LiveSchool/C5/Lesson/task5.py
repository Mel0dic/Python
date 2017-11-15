def my_function():
	print("Hello From My Function")

def my_function_with_args(username, greeting):
	print("Hello, %s, From my Function! I wish you %s" %(username, greeting))

my_function()

my_function_with_args(input("Enter your username: "), input("Enter a greeting: "))