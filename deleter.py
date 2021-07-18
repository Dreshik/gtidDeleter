print("Удалятора строк до # запущен");
while True:
	lines = [] 
	while True:
	    line = input()
	    if line:
	    	lines.append(line)
	    else:
	        break
	for line in lines:
		splittedLines = line.split('#')
		print(splittedLines[1].strip())