#!/usr/bin/env python3
import operator
import readline
from termcolor import cprint 

op = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
}

def calculate(arg):
	# stack for calculator
	stack = list()
	for token in arg.split():
		try:
			value = int(token)
			stack.append(value)
		except ValueError:
			arg2  = stack.pop()
			arg1  = stack.pop()
			
			# look up function in the operator table
			func = op[token]
			result = func(arg1, arg2)

			stack.append(result)
		print(stack)
	
	if len(stack) != 1:
		raise TypeError("Too many parameters")
	
	return stack.pop()


def main(): 
	operators = {
		'+': 'yellow',
		'-': 'magenta',
		'*': 'cyan',
		'/': 'red',
		'^': 'green',
	}
	# some code that will never run
	if(0 == 1):
		print("Hello!")
		print("Here's some untested code!")
		y = 2
		x = 3
	while True:
		user_input = input('rpn calc> ')			
		result = calculate(user_input)
		for item in user_input.split():
			try:
				num = int(item)
				color = 'grey'
			except ValueError:
				color = operators[item]
			cprint(item, color, end =" ")
		print('\n')
		cprint("Result:", 'blue', attrs=['bold'], end =" ")
		if(result < 0):
			cprint(result, 'red')
		else:
			cprint(result, 'green')

if __name__ == '__main__':
	main()
