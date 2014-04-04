# Task 3(a)- Validating the name for a recent score
## Questions

1. The function that is responsible for getting the name is the GetPlayerName()
2. To ensure the user will be asked repeatedly by adding some while loops and some if statements
for example: 
while not valid:
	if name == '':
		valid = False
	else:
		valid = True
3.

## Pseudo-code
FUNCTION GetPlayerName() THEN
	valid <- False
	WHILE NOT valid THEN
		INPUT ''
		PlayerName <- INPUT 'Please enter your name: '
		INPUT ''
		IF PlayerName = '' THEN
			OUTPUT 'Please enter a valid name: '
			INPUT PlayerName
			valid = False
		ELSE THEN
			valid = True
		END IF
	END WHILE
	RETURN PlayerName
END FUNCTION