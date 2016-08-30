import sys

fph = open('hiragana.csv')
fpk = open('katakana.csv')

katakana = []
for line in fpk:
	line = line.replace('KATAKANA LETTER','')
	line = line.replace('SMALL','')
	line = line.replace('\n','').split(',')
	katakana.append(line)

hiragana = []
for line in fpk:
        line = line.replace('HIRAGANA LETTER','')
        line = line.replace('SMALL','')
        line = line.replace('\n','').split(',')
        hiragana.append(line)


print katakana
print hiragana
