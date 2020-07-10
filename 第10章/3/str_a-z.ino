int thisChar = 0xA0;

void setup () {
   Serial.begin (9600);
   Serial.print ("According to islower:\r") ;
   Serial.print (islower( 'p' ) ? "p is a" : "p is not a" );
   Serial.print ( " lowercase letter\r" );
   Serial.print ( islower( 'P') ? "P is a" : "P is not a") ;
   Serial.print ("lowercase letter\r");
   Serial.print (islower( '5' ) ? "5 is a" : "5 is not a" );
   Serial.print ( " lowercase letter\r" );
   Serial.print ( islower( '!' )? "! is a" : "! is not a") ;
   Serial.print ("lowercase letter\r");

   Serial.print ("\rAccording to isupper:\r") ;
   Serial.print (isupper ( 'D' ) ? "D is a" : "D is not an" );
   Serial.print ( " uppercase letter\r" );
   Serial.print ( isupper ( 'd' )? "d is a" : "d is not an") ;
   Serial.print ( " uppercase letter\r" );
   Serial.print (isupper ( '8' ) ? "8 is a" : "8 is not an" );
   Serial.print ( " uppercase letter\r" );
   Serial.print ( islower( '$' )? "$ is a" : "$ is not an") ;
   Serial.print ("uppercase letter\r ");
}

void setup () {

}
