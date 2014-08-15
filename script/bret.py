#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#    Basic Regular Expressions Tester (BRET)
#    Copyright 2014 Hamza Abbad
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# Replacement function :
def replace(regexp, text, limit, start, end, replacement, exact):
	if exact :
		if exact_match(regexp, text, start, end) :
			modifiedText = replacement # Replace the selected text once.
			n = 1
		else : return (text, 0) # Don't replace anything.
	elif limit :
		modifiedText , n = regexp.subn(replacement, text[start:end], limit) # Replace the text from the start position to the end one with a specified limit.
	else :
		modifiedText, n = regexp.subn(replacement, text[start:end]) # Same as above, but without limit.
	text = text[:start]+modifiedText+text[end:] # The stripped beginning + selected text + the stripped end.
	return (text, n)
# Exact match function :
def exact_match(regexp, text, start, end):
	match = regexp.match(text[start:end])
	return match and match.group() == text[start:end]
# Searching function :
def search(regexp, text, limit, start, end):
	matches = [] # List of 'match' objects.
	if not limit : #  = "All" option
		matches = list(regexp.finditer(text, start, end)) # Create a list from an iterator of 'match' objects.
	else : # "Limit" option
		for i in range(limit): # Number of iterations = the limit of results requested.
			match = regexp.search(text, start, end)
			if match : matches.append(match); start = match.end()
			else : break
	return matches
# Splitting function :
def split(regexp, text, limit, start, end):
	return regexp.split(text[:start]+text[start:end]+text[end:], limit)
# If the script is running from the command line :
if __name__  == '__main__' :
	import sys
	if not (sys.version_info.major >= 3 and sys.version_info.minor >= 2 ):
		print('FATAL ERROR : Python 3.2 or later version is needed to run BRET', file=sys.stderr) # Because of argparse module.
		sys.exit(1) # (1) exit status is reserved for Python version error.
	import argparse
	import re
	parser = argparse.ArgumentParser(description='Basic Regular Expressions Tester')
	parser.add_argument('regexp', help='The regular expression pattern', metavar='RegExp')
	tig = parser.add_mutually_exclusive_group(required=True)
	tig.add_argument('-t', '--text', help='Text to be matched using the RegExp', metavar='Text')
	tig.add_argument('-i', '--input', help='Get the text from a file', metavar='File')
	parser.add_argument('-o', '--output', help='Write the results in a file', metavar='File')
	parser.add_argument('-r', '--replace', help='Replace matched text', metavar='Replacement')
	alg = parser.add_mutually_exclusive_group()
	alg.add_argument('-a', '--all', action='store_true', help='Return all matches')
	alg.add_argument('-l', '--limit', type=int, default='1', metavar='Limit')
	alg.add_argument('-x', '--exact-match', action='store_true', help='Check if the pattern match the string completely')
	parser.add_argument('-s', '--start', type=int, default='0', help='Set the starting position in the text', metavar='Position')
	parser.add_argument('-e', '--end', type=int, help='Set the ending position in the text', metavar='Position')
	parser.add_argument('-p', '--positions', action='store_true', help='Return the start and the end positions of the matches')
	parser.add_argument('-q', '--quite', action='store_true', help='Return the results only')
	parser.add_argument('-u', '--suppress-errors', action='store_true', help='Don\'t show error messages')
	parser.add_argument('-g', '--groups', action='store_true', help='Show matched groups also')
	parser.add_argument('-z', '--split', action='store_true', help='Split the text using a regular expression')
	args = parser.parse_args()
	if args.input :
		try:
			args.input = open(args.input, 'r', encoding="utf-8")
			args.text = args.input.read()
		except OSError as e:
			if not args.suppress_errors : print('ERROR : Couldn\'t read' , e.filename, ':', e.strerror, file=sys.stderr)
			sys.exit(3) # (3) exit status is reserved for file errors.
		args.input.close() # Send the file content to args.text variable in order to use it in the program.
	if args.output :
		try:
			args.output = open(args.output,'w', encoding="utf-8")
		except OSError as e:
			if not args.suppress_errors : print('ERROR : Couldn\'t write' , e.filename, ':', e.strerror, file=sys.stderr)
			sys.exit(3)
	else: args.output = sys.stdout
	n = len(args.text)
	if not args.end or args.end > n : args.end = n # Set the default value of --end option on the last position.
	if args.text[args.start:args.end]=='': args.start = args.end # Starting position mustn't be greater than the end.
	try:
		rx = re.compile(args.regexp) # Create the RegExp and check if it is valid.
	except re.error as e:
		if not args.suppress_errors : print('ERROR : invalid RegExp :', e.args[0], file=sys.stderr) # Print the error and exit with a non zero status.
		sys.exit(2); # (2) exit status is reserved for RegExp errors.
	if not args.quite and not args.output: print('') # Just an empty line before the main output.
	if args.all : args.limit = 0 # Set the limit to 0 (without limit) if 'all' option is specified.
	MATCH = 'Matched !' # Message to be displayed when the regular expression match the string and 'exact match' option is specified but not 'quite'.
	NO_MATCH = 'No match found !' # Message to be displayed when no matches are found and 'quite' option is not specified.
	if args.replace: # Replace option.
		text, n = replace(rx, args.text, args.limit, args.start, args.end, args.replace, args.exact_match)
		if not args.quite : print(n,'replacement'+('s' if n>1 else ''), 'made :', file=args.output)
		print(text, file=args.output)
		sys.exit(0)
	elif  args.split : # Split option.
		textParts = split(rx ,args.text, args.limit, args.start, args.end)
		n = len(textParts)-1
		if not args.quite :
			print(n, 'split'+('s' if n>1 else ''), 'made :', file=args.output)
		for part in textParts :
			print('-' if not args.quite else '', part, sep='', file=args.output)
	elif not args.exact_match : # Search option.
		matches = search(rx, args.text, args.limit, args.start, args.end)
		n = len(matches) # Number of matches found.
		if not args.quite and n>0:
			print(n,'match'+('es' if n>1 else ''), 'found :', file=args.output) # Write 'matches' if n > 1.
		for x in matches :
			print('-' if not args.quite else '', x.group(), ((((' : match from ' if not args.quite else '(') + str(x.start()) + (' to ' if not args.quite else ',') + str(x.end()) + (')' if args.quite else '')) if args.positions else '')), sep='', end=('|' if not args.quite else ''), file=args.output)
			if args.groups :
				print(' Groups :' if not args.quite else '', end=' ', file=args.output)
				for i in range(len(x.groups())) :
					print('('+str(i+1)+')' if not args.quite else '', x.group(i+1), sep='', end='/', file=args.output)
			print(file=args.output)
		if not n : # if there is no matches.
			if not args.quite: print(NO_MATCH, file=sys.stderr)
			sys.exit(4) # (4) exit status is reserved for 'No match' warnings.
	else : # "Exact match" option.
		matched = exact_match(rx, args.text, args.start, args.end)
		if matched :
			if not args.quite : print(MATCH, file=sys.stderr)
			sys.exit(0)
		else :
			if not args.quite : print(NO_MATCH, file=sys.stderr)
			sys.exit(4)
