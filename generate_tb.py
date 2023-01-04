from signal import *
import argparse
import os

## intialize command line parser
parser=argparse.ArgumentParser()
parser.add_argument("-o",help="output file name -o output_tb.v")
parser.add_argument("-v",help="pass verilog files to be lint")
args=parser.parse_args()

## opening Verilog file 
verilog_file=open(args.v,"r")
verilog_file2=open(args.v,"r")

file_txt=verilog_file.read()
file_lines=verilog_file2.readlines()
verilog_file.close()
verilog_file2.close()

## Search if module exist
name_start_index=module_exist(file_txt)

## Search if module has endmodule
endmodule_exist(file_txt)

## get module name
name_end_index=file_txt.find('(')
module_name=file_txt[name_start_index:name_end_index]
module_name.strip()

## create verilog module
module=verilog_module(module_name)
#print(module.get_name())

## find port list
portlist_end_index=file_txt.find(');')
if portlist_end_index==-1:
	print(bcolor.FAIL+bcolor.BOLD+bcolor.UNDERLINE+"ERROR:"+bcolor.ENDC+bcolor.FAIL+"Expecting ;"+bcolor.ENDC)
	exit()
portlist=file_txt[name_end_index+1:portlist_end_index]
	
#print(portlist)
signals_list=[]

## find port list signals 
port_list=portlist.split('\n')
for line in port_list:
	################# 	Get width	 #######################		
	index=line.find('[')
	if(index!=-1): #multi bit port 
		index2=line.find(']')
		port_len=line[index+1:index2]
		port_len=port_len.split(':')
		port_len=abs(int(port_len[1])-int(port_len[0]))+1
	else: 
		port_len=1;
	#####################		GET TYPE	 #######################
	if(line.find('input')!=-1): #input we don't care if it's reg or wire	
		line_signal_t=signal_t.input_t
	elif(line.find('output')!=-1):
		if(line.find('reg')!=-1):
			line_signal_t=signal_t.outputReg_t
			
		else:
			line_signal_t=signal_t.outputWire_t
	######################		GET NAMES	########################
	key_words=["input","output","wire","reg","signed","unsigned"]
	names=line.split(" ")
	for name in names:
		if any (x in name for x  in  key_words):
			pass
		else:
			if '[' in name:
				pass
			else:
				name=name.split(',')
				for x in name:
					if (x!=''):
						signals_list.append(signal(x,line_signal_t,port_len))
			
print(bcolor.OKGREEN+bcolor.BOLD+bcolor.UNDERLINE+"OK:"+bcolor.ENDC+bcolor.OKCYAN+"port list parsing is done"+bcolor.ENDC)
## define input signals 
f = open(args.o, "w")
f.close()
f = open(args.o, "a")
##TITLE LINE 
f.write("//*** test bench*** \n")
## Declerang TB signals 
f.write("//****************************** \n")
for s in signals_list:	
	if(s.get_signal_type()==signal_t.input_t):
		if(s.get_signal_width()==1):
			f.write("reg	"+s.get_signal_name()+"	; \n")
		else:
			w=s.get_signal_width()
			w=w-1
			f.write("reg	"+"["+str(w)+":0] "+s.get_signal_name()+"	; \n")
	else:
		if(s.get_signal_width()==1):
			f.write("wire	"+s.get_signal_name()+"	; \n")
		else:
			w=s.get_signal_width()
			w=w-1
			f.write("wire	"+"["+str(w)+":0] "+s.get_signal_name()+"	; \n")
f.write("\n \n//********* Module instantiation	*************** \n")
f.write("\n \n" +module_name + "DUT ( \n")
for s in signals_list:
	f.write("."+s.get_signal_name()+"	("+s.get_signal_name()+")	,\n")
f.close()
with open (args.o,'rb+') as filehandle:
	filehandle.seek(-2,os.SEEK_END)
	filehandle.truncate()
f.close()
f = open(args.o, "a")

f.write("\n ) ;\n")

f.write("\n \n//********* STIMULUS	*************** \n")
f.write("initial \n	begin \n")
f.write("\n	end")
f.close()
