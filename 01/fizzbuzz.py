import sys

# @param msg str
def print_noln( msg ):
    sys.stdout.write( msg )


# @param myRange range
def FizzBuzz( myRange ):
    for x in myRange:
        mult_of_3 = x % 3 == 0
        mult_of_5 = x % 5 == 0
        if mult_of_3:
            print_noln( 'Fizz' )
        if mult_of_5:
            print_noln( 'Buzz' )
        if not mult_of_3 and not mult_of_5:
            print_noln( str( x ) )
        print_noln( '\n' )

FizzBuzz( range( 1, 101 ) )
