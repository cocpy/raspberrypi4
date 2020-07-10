void setup () {
   Serial.begin (9600);
   Serial.print ( " According to isspace:\rNewline ") ;
   Serial.print (isspace( '\n' )? " is a" : " is not a" );
   Serial.print ( " whitespace character\rHorizontal tab") ;
   Serial.print (isspace( '\t' )? " is a" : " is not a" );
   Serial.print ( " whitespace character\n") ;
   Serial.print (isspace('%')? " % is a" : " % is not a" );

   Serial.print ( " \rAccording to iscntrl:\rNewline") ;
   Serial.print ( iscntrl( '\n' )?"is a" : " is not a" ) ;
   Serial.print (" control character\r");
   Serial.print (iscntrl( '$' ) ? " $ is a" : " $ is not a" );
   Serial.print (" control character\r");
   Serial.print ("\rAccording to ispunct:\r");
   Serial.print (ispunct(';' ) ?"; is a" : "; is not a" ) ;
   Serial.print (" punctuation character\r");
   Serial.print (ispunct('Y' ) ?"Y is a" : "Y is not a" ) ;
   Serial.print ("punctuation character\r");
   Serial.print (ispunct('#' ) ?"# is a" : "# is not a" ) ;
   Serial.print ("punctuation character\r");

   Serial.print ( "\r According to isprint:\r");
   Serial.print (isprint('$' ) ?"$ is a" : "$ is not a" );
   Serial.print (" printing character\rAlert ");
   Serial.print (isprint('\a' ) ?" is a" : " is not a" );
   Serial.print (" printing character\rSpace ");
   Serial.print (isprint(' ' ) ?" is a" : " is not a" );
   Serial.print (" printing character\r");

   Serial.print ("\r According to isgraph:\r");
   Serial.print (isgraph ('Q' ) ?"Q is a" : "Q is not a" );
   Serial.print ("printing character other than a space\rSpace ");
   Serial.print (isgraph (' ') ?" is a" : " is not a" );
   Serial.print ("printing character other than a space ");
}

void loop () {

}
