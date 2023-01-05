//*** test bench*** 
//****************************** 

 
 module tb_test() ; 
reg	[4:0] a	; 
reg	[4:0] b	; 
reg	[4:0] c	; 
reg	[4:0] d	; 
wire	[5:0] result1	; 
wire	[5:0] result2	; 

 
//********* Module instantiation	*************** 

 
 test DUT ( 
.a	(a)	,
.b	(b)	,
.c	(c)	,
.d	(d)	,
.result1	(result1)	,
.result2	(result2)	
 ) ;

 
//********* STIMULUS	*************** 
initial 
	begin 

	integer i;
 	for (i=0;i<20;i=i+1) 
		begin

 
//********* Random inputs generation	*************** 
			a = $random();
			#10;
			b = $random();
			#10;
			c = $random();
			#10;
			d = $random();
			#10;

 
//********* MONITOR	*************** 
			$display("******* %t  ********",$time);
			$display("%d",a); 
			$display("%d",b); 
			$display("%d",c); 
			$display("%d",d); 
			$display("%d",result1); 
			$display("%d",result2); 

		end
	end
endmodule