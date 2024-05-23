#strip() :- using split string
x='abcd,xyz'
x.split(',')
print(x)

x='abcd 9xyz'
x.split('9')
print(x)

#space:-
x='abcd         xyz'
x.split(' ')
print(x)

#strip :-text value remove
x='                     abc,wer                    '
x.strip()
print(x)

x='hello'
y=x.upper()
print(y)

x='HELLO'
y=x.lower()
print(y)

x= "hello mr abc"
y=x.capitalize()
print(y)

x="bablumaraathe"
y=x.capitalize()
print(y)  