import re

# Signal class
# Signal available states Enumuration 
class signal_t:
	'''
	Signal available states Enumuration
	'''
	input_t=1
	outputReg_t=2
	outputWire_t=3
	netWire_t=4
	netReg_t=5

class signal:

	# init method or constructor
	def __init__(self, name,signalType,width):
		self.__name = name
		self.__signalType=signalType
		self.__width=width
		self.driven=0

	# Methods
	def print_signal(self):
		print("****************************")
		print("my name is",self.__name)
		print("my type is",self.__signalType)
		print("my width is",self.__width)
		print("Am I driven?",self.driven)
	def check_if_driven(self):
		'''
		this function check if a signal is driven or not
		it return 0 if not driven and 1 if driven
		'''
		return self.__driven
		
	def get_signal_width(self):
		return self.__width
		
	def get_signal_name(self):
		return self.__name
	def get_signal_type(self):
		return self.__signalType	
class verilog_module:

	# init method or constructor
	def __init__(self, name):
		self.__name = name
		self.correct_port_list=0
	
	def get_name(self):

		return self.__name

class bcolor:
	HEADER='\033[95m'
	OKBLUE='\033[94m'
	OKCYAN='\033[96m'
	OKGREEN='\033[92m'
	WARNING='\033[93m'
	FAIL='\033[91m'
	ENDC='\033[0m'
	BOLD='\033[1m'
	UNDERLINE='\033[4m'
	
def module_exist(x):
	match=re.search(r' *module',x)
	if (match==None):
		print(bcolor.FAIL+bcolor.BOLD+bcolor.UNDERLINE+"ERROR:"+bcolor.ENDC+bcolor.FAIL+"NO MODULES FOUND"+bcolor.ENDC)
		exit()		
	return match.end()	
def endmodule_exist(x):
	match=re.search(r' *endmodule',x)
	if (match==None):
		print(bcolor.FAIL+bcolor.BOLD+bcolor.UNDERLINE+"ERROR:"+bcolor.ENDC+bcolor.FAIL+"MISSING MODULE END"+bcolor.ENDC)
		
		

