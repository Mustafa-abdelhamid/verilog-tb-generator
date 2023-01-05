//*** test bench*** 
//****************************** 

 
 module tb_mux() ; 
reg	a	; 
reg	b	; 
reg	c	; 
reg	d;	; 
reg	s0	; 
reg	s1;	; 
wire	out	; 

 
//********* Module instantiation	*************** 

 
 mux DUT ( 
.a	(a)	,
.b	(b)	,
.c	(c)	,
.d;	(d;)	,
.s0	(s0)	,
.s1;	(s1;)	,
.out	(out)	
 ) ;

 
//********* STIMULUS	*************** 
initial 
	begin 

	integer i;
 	for (i=0;i<100;i=i+1) 
		begin

 
//********* Random inputs generation	*************** 
			a = $random();
			b = $random();
			c = $random();
			d; = $random();
			s0 = $random();
			s1; = $random();

			#10;
 
//********* MONITOR	*************** 
			$display("******* %t  ********",$time);
			$display("%d",a); 
			$display("%d",b); 
			$display("%d",c); 
			$display("%d",d;); 
			$display("%d",s0); 
			$display("%d",s1;); 
			$display("%d",out); 

		end
	end
endmodule