void setup () {
   Serial.begin (9600);
   Serial.print ("According to isdigit:\r");
   Serial.print (isdigit( '8' ) ? "8 is a": "8 is not a");
   Serial.print (" digit\r" );
   Serial.print (isdigit( '8' ) ?"# is a": "# is not a") ;
   Serial.print (" digit\r");
   Serial.print ("\rAccording to isalpha:\r" );
   Serial.print (isalpha('A' ) ?"A is a": "A is not a");
   Serial.print (" letter\r");
   Serial.print (isalpha('A' ) ?"b is a": "b is not a");
   Serial.print (" letter\r");
   Serial.print (isalpha('A') ?"& is a": "& is not a");
   Serial.print (" letter\r");
   Serial.print (isalpha( 'A' ) ?"4 is a":"4 is not a");
   Serial.print (" letter\r");
   Serial.print ("\rAccording to isalnum:\r");
   Serial.print (isalnum( 'A' ) ?"A is a" : "A is not a" );

   Serial.print (" digit or a letter\r" );
   Serial.print (isalnum( '8' ) ?"8 is a" : "8 is not a" ) ;
   Serial.print (" digit or a letter\r");
   Serial.print (isalnum( '#' ) ?"# is a" : "# is not a" );
   Serial.print (" digit or a letter\r");
   Serial.print ("\rAccording to isxdigit:\r");
   Serial.print (isxdigit( 'F' ) ?"F is a" : "F is not a" );
   Serial.print (" hexadecimal digit\r" );
   Serial.print (isxdigit( 'J' ) ?"J is a" : "J is not a" ) ;
   Serial.print (" hexadecimal digit\r" );
   Serial.print (isxdigit( '7' ) ?"7 is a" : "7 is not a" ) ;

   Serial.print (" hexadecimal digit\r" );
   Serial.print (isxdigit( '$' ) ? "$ is a" : "$ is not a" );
   Serial.print (" hexadecimal digit\r" );
   Serial.print (isxdigit( 'f' ) ? "f is a" : "f is not a");

}

void loop () {

}
