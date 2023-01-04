//*** test bench*** 
//****************************** 
reg	[4:0] a	; 
reg	[4:0] b	; 
wire	[5:0] result	; 

 
//********* Module instantiation	*************** 

 
 test DUT ( 
.a	(a)	,
.b	(b)	,
.result	(result)	
 ) ;

 
//********* STIMULUS	*************** 
initial 
	begin 

	end